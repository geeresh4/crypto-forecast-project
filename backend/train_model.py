# train_model.py
# Trains LSTM models for cryptocurrency price prediction

import pandas as pd
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
import pickle

DATA_DIR = "backend/data"
MODELS_DIR = "backend/models"

def ensure_models_directory():
    """Ensure models directory exists"""
    os.makedirs(MODELS_DIR, exist_ok=True)

def load_data(symbol):
    """Load historical data for a coin"""
    csv_path = os.path.join(DATA_DIR, f"{symbol}.csv")
    
    if not os.path.exists(csv_path):
        print(f"No data file found for {symbol}")
        return None
    
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    return df

def prepare_sequences(data, lookback=60):
    """Prepare sequences for LSTM training"""
    # Use 'price' column for prediction
    prices = data['price'].values.reshape(-1, 1)
    
    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(prices)
    
    X, y = [], []
    for i in range(lookback, len(scaled_prices)):
        X.append(scaled_prices[i-lookback:i, 0])
        y.append(scaled_prices[i, 0])
    
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    # Split into train and test (80/20)
    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    return X_train, X_test, y_train, y_test, scaler

def build_lstm_model(input_shape):
    """Build LSTM model architecture"""
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=True),
        Dropout(0.2),
        LSTM(50),
        Dropout(0.2),
        Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    
    return model

def train_model_for_coin(symbol, epochs=50, batch_size=32, lookback=60):
    """Train LSTM model for a specific coin"""
    print(f"Training model for {symbol}...")
    
    # Load data
    data = load_data(symbol)
    if data is None or len(data) < lookback + 100:
        print(f"Insufficient data for {symbol}. Need at least {lookback + 100} records.")
        return False
    
    # Prepare sequences
    X_train, X_test, y_train, y_test, scaler = prepare_sequences(data, lookback)
    
    if len(X_train) == 0:
        print(f"Not enough data to create sequences for {symbol}")
        return False
    
    # Build model
    model = build_lstm_model((X_train.shape[1], 1))
    
    # Early stopping
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    
    # Train model
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_test, y_test),
        callbacks=[early_stopping],
        verbose=1
    )
    
    # Save model
    model_path = os.path.join(MODELS_DIR, f"{symbol}_model.h5")
    model.save(model_path)
    print(f"Model saved to {model_path}")
    
    # Save scaler
    scaler_path = os.path.join(MODELS_DIR, f"{symbol}_scaler.pkl")
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)
    print(f"Scaler saved to {scaler_path}")
    
    return True

def train_all_models():
    """Train models for all available coins"""
    ensure_models_directory()
    
    if not os.path.exists(DATA_DIR):
        print(f"Data directory {DATA_DIR} does not exist. Please run collect_data.py first.")
        return
    
    # Get all CSV files in data directory
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        print("No data files found. Please run collect_data.py first.")
        return
    
    for csv_file in csv_files:
        symbol = csv_file.replace('.csv', '')
        train_model_for_coin(symbol, epochs=30, batch_size=32)

if __name__ == "__main__":
    train_all_models()
    print("Model training complete!")
