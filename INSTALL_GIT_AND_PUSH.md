# Install Git and Push to GitHub - Step by Step

## Step 1: Install Git

### Option A: Download Git for Windows (Recommended)

1. **Download Git**:
   - Go to: https://git-scm.com/download/win
   - Click "Download for Windows"
   - The download will start automatically

2. **Install Git**:
   - Run the downloaded installer (Git-2.x.x-64-bit.exe)
   - Click "Next" through all screens (default settings are fine)
   - **Important**: Make sure "Git from the command line and also from 3rd-party software" is selected
   - Click "Install"
   - Wait for installation to complete
   - Click "Finish"

3. **Verify Installation**:
   - Close and reopen PowerShell/Terminal
   - Run: `git --version`
   - You should see: `git version 2.x.x`

### Option B: Install via Winget (Windows Package Manager)

If you have Windows 10/11 with winget:
```powershell
winget install --id Git.Git -e --source winget
```

### Option C: Install via Chocolatey

If you have Chocolatey installed:
```powershell
choco install git
```

## Step 2: Configure Git (First Time Only)

Open PowerShell and run:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

## Step 3: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new
2. **Repository Settings**:
   - Repository name: `crypto-forecast-project`
   - Description: "Cryptocurrency price forecasting system using LSTM models"
   - Visibility: **Public** (or Private if you prefer)
   - **DO NOT** check "Initialize with README"
   - **DO NOT** add .gitignore or license
3. **Click "Create repository"**

## Step 4: Push Code to GitHub

After Git is installed, run these commands in PowerShell (in your project directory):

```powershell
# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Crypto Forecast Project - Complete implementation

- Complete folder structure with frontend and backend
- FastAPI backend with authentication, coin listing, history, and prediction endpoints
- LSTM model training scripts
- Data collection from CoinGecko API and CSV processing
- Modern frontend with animated UI
- User authentication system
- Price prediction functionality
- Render deployment configuration"

# Add remote repository
git remote add origin https://github.com/geeresh4/crypto-forecast-project.git

# Set branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note**: When pushing, you'll be prompted for credentials:
- **Username**: `geeresh4`
- **Password**: Use a **Personal Access Token** (not your GitHub password)
  - Generate token: https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Name: "Crypto Forecast Project"
  - Select scope: `repo` (full control of private repositories)
  - Click "Generate token"
  - **Copy the token** (you won't see it again!)
  - Use this token as your password when pushing

## Alternative: Use Automated Script

After installing Git, you can use the automated script:

```powershell
.\push_to_github.ps1
```

This script will:
- Check if Git is installed
- Initialize repository
- Add all files
- Create commit
- Guide you through creating the GitHub repo
- Push the code

## Troubleshooting

### Git command not found after installation
- **Solution**: Close and reopen PowerShell/Terminal
- Or restart your computer
- Or add Git to PATH manually

### Authentication failed
- **Solution**: Use Personal Access Token instead of password
- Generate token: https://github.com/settings/tokens
- Select `repo` scope

### Repository already exists
- **Solution**: The script will detect it, or manually add remote:
  ```powershell
  git remote add origin https://github.com/geeresh4/crypto-forecast-project.git
  ```

### Push rejected
- **Solution**: Make sure repository exists on GitHub
- Check you have write access
- Try: `git push -u origin main --force` (use with caution)

## Quick Checklist

- [ ] Git installed
- [ ] Git configured (name and email)
- [ ] GitHub repository created
- [ ] Personal Access Token generated
- [ ] Code pushed to GitHub

## After Pushing

Once code is pushed, you can:
1. View your repository: https://github.com/geeresh4/crypto-forecast-project
2. Proceed to Render deployment (see `RENDER_DEPLOYMENT.md`)

