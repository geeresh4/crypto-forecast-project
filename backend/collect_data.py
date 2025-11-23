# collect_data.py
# Collects historical cryptocurrency data from CoinGecko API or processes existing CSV

import pandas as pd
import requests
import os
import time
from datetime import datetime, timedelta

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
COINGECKO_API = "https://api.coingecko.com/api/v3"

def ensure_data_directory():
    """Ensure data directory exists"""
    os.makedirs(DATA_DIR, exist_ok=True)

def process_existing_csv(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join(PROJECT_ROOT, "Cryptocurrency_Price_Forecasting_Extended.csv")
    """Process the existing CSV file and split by coin"""
    if not os.path.exists(csv_path):
        print(f"CSV file {csv_path} not found. Will use CoinGecko API instead.")
        return False
    
    print("Processing existing CSV file...")
    try:
        df = pd.read_csv(csv_path)
        
        # Group by coin symbol
        for symbol in df['coinsymbol'].unique():
            coin_data = df[df['coinsymbol'] == symbol].copy()
            
            # Sort by date
            coin_data['date'] = pd.to_datetime(coin_data['date'])
            coin_data = coin_data.sort_values('date')
            
            # Select relevant columns
            output_df = coin_data[['date', 'open', 'high', 'low', 'close', 'price', 'volume', 'marketcap']].copy()
            
            # Save to CSV
            output_path = os.path.join(DATA_DIR, f"{symbol}.csv")
            output_df.to_csv(output_path, index=False)
            print(f"Saved {len(output_df)} records for {symbol} to {output_path}")
        
        return True
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return False

def fetch_coin_data_from_coingecko(coin_id, symbol, days=3650):
    """Fetch historical data from CoinGecko API"""
    try:
        print(f"Fetching data for {symbol} from CoinGecko...")
        
        # Get historical market data
        url = f"{COINGECKO_API}/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days,
            "interval": "daily"
        }
        
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Process prices
        prices = data.get('prices', [])
        market_caps = data.get('market_caps', [])
        volumes = data.get('total_volumes', [])
        
        if not prices:
            print(f"No data found for {symbol}")
            return None
        
        # Create DataFrame
        df_data = []
        for i, price_point in enumerate(prices):
            timestamp = price_point[0]
            price = price_point[1]
            market_cap = market_caps[i][1] if i < len(market_caps) else 0
            volume = volumes[i][1] if i < len(volumes) else 0
            
            date = datetime.fromtimestamp(timestamp / 1000)
            
            df_data.append({
                'date': date,
                'open': price,  # Using price as open/close/high/low (CoinGecko limitation)
                'high': price,
                'low': price,
                'close': price,
                'price': price,
                'volume': volume,
                'marketcap': market_cap
            })
        
        df = pd.DataFrame(df_data)
        df = df.sort_values('date')
        
        # Save to CSV
        output_path = os.path.join(DATA_DIR, f"{symbol}.csv")
        df.to_csv(output_path, index=False)
        print(f"Saved {len(df)} records for {symbol} to {output_path}")
        
        # Rate limiting
        time.sleep(1)
        
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def collect_top_coins():
    """Collect data for top 10 cryptocurrencies"""
    ensure_data_directory()
    
    # First, try to process existing CSV
    if process_existing_csv():
        print("Successfully processed existing CSV file.")
        return
    
    # If CSV processing fails, use CoinGecko API
    print("Using CoinGecko API to fetch data...")
    
    # Top 10 coins by market cap
    top_coins = [
        {"id": "bitcoin", "symbol": "BTC"},
        {"id": "ethereum", "symbol": "ETH"},
        {"id": "binancecoin", "symbol": "BNB"},
        {"id": "ripple", "symbol": "XRP"},
        {"id": "cardano", "symbol": "ADA"},
        {"id": "solana", "symbol": "SOL"},
        {"id": "dogecoin", "symbol": "DOGE"},
        {"id": "polkadot", "symbol": "DOT"},
        {"id": "polygon", "symbol": "MATIC"},
        {"id": "litecoin", "symbol": "LTC"}
    ]
    
    for coin in top_coins:
        fetch_coin_data_from_coingecko(coin["id"], coin["symbol"])
        time.sleep(1)  # Rate limiting

if __name__ == "__main__":
    collect_top_coins()
    print("Data collection complete!")
