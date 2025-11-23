# GitHub Setup Instructions

## Prerequisites
1. Install Git if not already installed: https://git-scm.com/download/win
2. Create a GitHub account if you don't have one: https://github.com

## Steps to Push to GitHub

1. **Initialize Git Repository** (if not already done):
```bash
git init
```

2. **Configure Git** (if first time):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

3. **Add All Files**:
```bash
git add .
```

4. **Create Initial Commit**:
```bash
git commit -m "Initial commit: Crypto Forecast Project - Complete implementation"
```

5. **Create Repository on GitHub**:
   - Go to https://github.com/geeresh4
   - Click "New repository"
   - Name it (e.g., "crypto-forecast-project")
   - Do NOT initialize with README, .gitignore, or license
   - Click "Create repository"

6. **Add Remote and Push**:
```bash
git remote add origin https://github.com/geeresh4/crypto-forecast-project.git
git branch -M main
git push -u origin main
```

## Alternative: Using GitHub CLI

If you have GitHub CLI installed:
```bash
gh repo create crypto-forecast-project --public --source=. --remote=origin --push
```

## Project Structure

The project includes:
- ✅ Complete folder structure
- ✅ Frontend (HTML, CSS, JavaScript)
- ✅ Backend (FastAPI with all endpoints)
- ✅ ML model training scripts
- ✅ Data collection scripts
- ✅ User authentication system
- ✅ Coin listing and history endpoints
- ✅ Prediction API with LSTM models

## Next Steps After Push

1. **Process Historical Data**:
```bash
cd backend
python collect_data.py
```

2. **Train Models**:
```bash
python train_model.py
```

3. **Start Backend Server**:
```bash
python app.py
```

4. **Open Frontend**:
   - Open `frontend/index.html` in a web browser
   - Or use a local server: `python -m http.server 8080` in the frontend directory

