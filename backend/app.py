from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import json
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

# Optional ML imports - handle gracefully if not available
try:
    import pickle
    from tensorflow.keras.models import load_model
    from sklearn.preprocessing import MinMaxScaler
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    print("Warning: ML dependencies not available. Prediction features will be limited.")

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database path - adjust for Render deployment
if os.path.exists("backend/database"):
    DB_PATH = "backend/database/users.json"
    DATA_DIR = "backend/data"
    MODELS_DIR = "backend/models"
    PREDICTIONS_DIR = "backend/predictions"
else:
    # For Render deployment (when running from backend directory)
    DB_PATH = "database/users.json"
    DATA_DIR = "data"
    MODELS_DIR = "models"
    PREDICTIONS_DIR = "predictions"

COINGECKO_API = "https://api.coingecko.com/api/v3"

# Pydantic models
class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str
    country: str

class LoginRequest(BaseModel):
    username: str
    password: str

class PredictionRequest(BaseModel):
    coin: str
    start: str
    end: str

# Initialize users.json if it doesn't exist
def init_database():
    if not os.path.exists(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH, 'w') as f:
            json.dump({"users": []}, f)

init_database()

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(PREDICTIONS_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Crypto Forecast API"}

@app.post("/register")
async def register(user: RegisterRequest):
    """Register a new user"""
    try:
        with open(DB_PATH, 'r') as f:
            data = json.load(f)
        
        # Check if username or email already exists
        for existing_user in data.get("users", []):
            if existing_user.get("username") == user.username:
                raise HTTPException(status_code=400, detail="Username already exists")
            if existing_user.get("email") == user.email:
                raise HTTPException(status_code=400, detail="Email already exists")
        
        # Add new user
        new_user = {
            "email": user.email,
            "username": user.username,
            "password": user.password,  # In production, hash this!
            "country": user.country,
            "created_at": datetime.now().isoformat()
        }
        
        data["users"].append(new_user)
        
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, indent=2)
        
        return {"message": "User registered successfully", "username": user.username}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
async def login(credentials: LoginRequest):
    """Login user"""
    try:
        with open(DB_PATH, 'r') as f:
            data = json.load(f)
        
        for user in data.get("users", []):
            if user.get("username") == credentials.username:
                if user.get("password") == credentials.password:
                    return {
                        "message": "Login successful",
                        "username": credentials.username,
                        "token": f"token_{credentials.username}_{datetime.now().timestamp()}"  # Simple token
                    }
                else:
                    raise HTTPException(status_code=401, detail="Invalid password")
        
        raise HTTPException(status_code=404, detail="User not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/coins")
async def get_coins():
    """Get top 10 coins sorted by market cap"""
    try:
        # Try to get data from CoinGecko API
        url = f"{COINGECKO_API}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 10,
            "page": 1,
            "sparkline": False
        }
        
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            coins = []
            for coin in data:
                coins.append({
                    "name": coin.get("name", ""),
                    "symbol": coin.get("symbol", "").upper(),
                    "price": coin.get("current_price", 0),
                    "change_24h": coin.get("price_change_percentage_24h", 0)
                })
            return {"coins": coins}
        else:
            # Fallback: get from local data files
            return get_coins_from_local_data()
    except Exception as e:
        # Fallback: get from local data files
        return get_coins_from_local_data()

def get_coins_from_local_data():
    """Get coins from local CSV files"""
    coins = []
    coin_names = {
        "BTC": "Bitcoin",
        "ETH": "Ethereum",
        "BNB": "Binance Coin",
        "XRP": "Ripple",
        "ADA": "Cardano",
        "SOL": "Solana",
        "DOGE": "Dogecoin",
        "DOT": "Polkadot",
        "MATIC": "Polygon",
        "LTC": "Litecoin"
    }
    
    for symbol, name in coin_names.items():
        csv_path = os.path.join(DATA_DIR, f"{symbol}.csv")
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                if len(df) > 0:
                    latest = df.iloc[-1]
                    # Calculate 24h change if we have enough data
                    change_24h = 0
                    if len(df) >= 2:
                        prev_price = df.iloc[-2]['price']
                        curr_price = latest['price']
                        if prev_price > 0:
                            change_24h = ((curr_price - prev_price) / prev_price) * 100
                    
                    coins.append({
                        "name": name,
                        "symbol": symbol,
                        "price": float(latest.get('price', 0)),
                        "change_24h": round(change_24h, 2)
                    })
            except:
                pass
    
    # Sort by price (as proxy for market cap)
    coins.sort(key=lambda x: x['price'], reverse=True)
    return {"coins": coins[:10]}

@app.get("/history/{coin}")
async def get_history(coin: str):
    """Get last 30-day prices for a coin"""
    coin = coin.upper()
    csv_path = os.path.join(DATA_DIR, f"{coin}.csv")
    
    if not os.path.exists(csv_path):
        raise HTTPException(status_code=404, detail=f"No data found for {coin}")
    
    try:
        df = pd.read_csv(csv_path)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # Get last 30 days
        if len(df) > 30:
            df = df.tail(30)
        
        history = []
        for _, row in df.iterrows():
            history.append({
                "date": row['date'].strftime('%Y-%m-%d'),
                "price": float(row.get('price', 0))
            })
        
        return {
            "coin": coin,
            "history": history
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
async def predict(request: PredictionRequest):
    """Generate predictions for a coin"""
    coin = request.coin.upper()
    start = request.start
    end = request.end
    
    # Check if ML dependencies are available
    if not ML_AVAILABLE:
        raise HTTPException(
            status_code=503,
            detail="ML prediction features are not available. TensorFlow is not installed. Please install ML dependencies or use a service with TensorFlow support."
        )
    
    try:
        # Parse dates
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        
        if start_date >= end_date:
            raise HTTPException(status_code=400, detail="Start date must be before end date")
        
        # Check if model exists
        model_path = os.path.join(MODELS_DIR, f"{coin}_model.h5")
        scaler_path = os.path.join(MODELS_DIR, f"{coin}_scaler.pkl")
        
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            raise HTTPException(
                status_code=404, 
                detail=f"Model not found for {coin}. Please train the model first."
            )
        
        # Load model and scaler
        from tensorflow.keras.models import load_model
        import pickle
        from sklearn.preprocessing import MinMaxScaler
        
        model = load_model(model_path)
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        
        # Load historical data
        csv_path = os.path.join(DATA_DIR, f"{coin}.csv")
        if not os.path.exists(csv_path):
            raise HTTPException(status_code=404, detail=f"No data found for {coin}")
        
        df = pd.read_csv(csv_path)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # Get last 60 days for prediction input
        lookback = 60
        if len(df) < lookback:
            raise HTTPException(status_code=400, detail=f"Insufficient historical data for {coin}")
        
        recent_data = df.tail(lookback)['price'].values.reshape(-1, 1)
        scaled_data = scaler.transform(recent_data)
        
        # Generate predictions
        predictions = []
        current_date = start_date
        prediction_input = scaled_data[-lookback:].reshape(1, lookback, 1)
        
        while current_date <= end_date:
            # Predict next day
            next_pred = model.predict(prediction_input, verbose=0)
            next_price = scaler.inverse_transform(next_pred)[0][0]
            
            predictions.append({
                "date": current_date.strftime('%Y-%m-%d'),
                "price": round(float(next_price), 2)
            })
            
            # Update input for next prediction
            next_scaled = scaler.transform([[next_price]])
            prediction_input = np.append(prediction_input[0][1:], next_scaled).reshape(1, lookback, 1)
            
            current_date += timedelta(days=1)
        
        # Save predictions to CSV
        predictions_df = pd.DataFrame(predictions)
        predictions_filename = f"{coin}_{start}_to_{end}.csv"
        predictions_path = os.path.join(PREDICTIONS_DIR, predictions_filename)
        predictions_df.to_csv(predictions_path, index=False)
        
        return {
            "coin": coin,
            "start": start,
            "end": end,
            "predictions": predictions
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

