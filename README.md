# Crypto Forecast Project

A cryptocurrency price forecasting system using LSTM/RNN models for time-series prediction.

## Project Structure

```
crypto-forecast-project/
│
├─ backend/
│   ├─ app.py                 # FastAPI backend server
│   ├─ train_model.py         # ML model training script
│   ├─ collect_data.py        # Data collection from CoinGecko API
│   ├─ requirements.txt       # Python dependencies
│   ├─ database/
│   │   └─ users.json         # User database (JSON)
│   ├─ models/                # Trained ML models
│   ├─ data/                  # Historical CSV data
│   └─ predictions/           # Generated prediction CSVs
│
├─ frontend/
│   ├─ index.html             # Home page
│   ├─ login.html             # Login page
│   ├─ register.html          # Registration page
│   ├─ dashboard.html         # Dashboard with top coins
│   ├─ prediction.html        # Prediction interface
│   ├─ css/
│   │   ├─ style.css          # Main stylesheet
│   │   ├─ login.css          # Login/Register styles
│   │   └─ dashboard.css      # Dashboard/Prediction styles
│   └─ js/
│       ├─ main.js            # Main JavaScript
│       ├─ login.js           # Login functionality
│       ├─ register.js        # Registration functionality
│       ├─ dashboard.js       # Dashboard functionality
│       └─ prediction.js      # Prediction functionality
│
└─ README.md
```

## Features

- **User Authentication**: Register and login system
- **Coin Dashboard**: View top 10 cryptocurrencies by market cap
- **Price History**: View 30-day price history for any coin
- **Price Predictions**: Generate LSTM-based price forecasts
- **Animated UI**: Modern, responsive design with animated backgrounds

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
python app.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Open the frontend files in a web browser or use a local server:
```bash
# Using Python's built-in server
cd frontend
python -m http.server 8080
```

2. Navigate to `http://localhost:8080` in your browser

## API Endpoints

- `POST /register` - Register a new user
- `POST /login` - Login user
- `GET /coins` - Get top 10 coins
- `GET /history/{coin}` - Get coin price history
- `POST /predict?coin={symbol}&start={date}&end={date}` - Generate predictions

## Development Phases

### Phase 1: ✅ Project Setup & Folder Structure
- Complete folder structure created
- All HTML, CSS, and JS files with boilerplate
- FastAPI backend skeleton with all endpoints
- User database (users.json) initialized

### Phase 2: ✅ ML Model, Data Collection & API Development
- Data collection from CoinGecko API (with CSV processing fallback)
- LSTM model training implementation
- Full prediction API implementation
- Complete authentication system
- Coin history and listing endpoints

### Phase 3: ✅ Frontend Development & Full Integration
- Complete UI with animations
- Form validation
- Dynamic data rendering
- Full frontend-backend integration

### Phase 4: GitHub Push
To push to GitHub, follow these steps:

1. **Install Git** (if not installed): https://git-scm.com/download/win

2. **Run the setup script**:
   ```bash
   setup_git.bat
   ```
   
   Or manually:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Crypto Forecast Project"
   ```

3. **Create repository on GitHub**:
   - Go to https://github.com/geeresh4
   - Create a new repository (e.g., "crypto-forecast-project")

4. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/geeresh4/REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

See `GITHUB_SETUP.md` for detailed instructions.

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python, FastAPI
- **ML**: TensorFlow/Keras (LSTM/RNN)
- **Database**: JSON file (users), CSV files (data/predictions)
- **Data Source**: CoinGecko API

## Notes

- The CSV file `Cryptocurrency_Price_Forecasting_Extended.csv` in the root directory can be used for training if needed
- All passwords are stored in plain text (for development only - hash in production!)
- Models will be saved in `backend/models/` directory
- Predictions will be saved as CSV files in `backend/predictions/`

