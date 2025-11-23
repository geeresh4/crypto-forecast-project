# Quick Start Guide - Push to GitHub

## Option 1: Automated Script (Recommended)

1. **Install Git** (if not installed):
   - Download from: https://git-scm.com/download/win
   - Install with default settings

2. **Run the automated script**:
   ```powershell
   .\push_to_github.ps1
   ```

   The script will:
   - Check for Git installation
   - Initialize the repository
   - Add all files
   - Create a commit
   - Guide you to create the GitHub repository
   - Push the code

## Option 2: Manual Steps

### Step 1: Install Git
Download and install from: https://git-scm.com/download/win

### Step 2: Create GitHub Repository
1. Go to: https://github.com/new
2. Repository name: `crypto-forecast-project`
3. Description: "Cryptocurrency price forecasting system using LSTM models"
4. Set to **Public** (or Private)
5. **DO NOT** check "Initialize with README"
6. Click "Create repository"

### Step 3: Initialize and Push
Open PowerShell in the project directory and run:

```powershell
# Initialize Git
git init

# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Create commit
git commit -m "Initial commit: Crypto Forecast Project - Complete implementation"

# Add remote (replace with your actual repo name if different)
git remote add origin https://github.com/geeresh4/crypto-forecast-project.git

# Set branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note**: When pushing, you'll be prompted for credentials:
- Username: `geeresh4`
- Password: Use a **Personal Access Token** (not your GitHub password)
  - Generate token: https://github.com/settings/tokens
  - Select scope: `repo` (full control of private repositories)

## Verification

After pushing, visit:
https://github.com/geeresh4/crypto-forecast-project

You should see all your project files!

## Troubleshooting

### Git not found
- Install Git from https://git-scm.com/download/win
- Restart your terminal/PowerShell after installation

### Authentication failed
- Use Personal Access Token instead of password
- Generate token: https://github.com/settings/tokens
- Select `repo` scope

### Repository already exists
- If you already created the repo, the script will detect it
- Or manually add remote: `git remote add origin https://github.com/geeresh4/REPO_NAME.git`

### Push rejected
- Make sure the repository exists on GitHub
- Check that you have write access
- Try: `git push -u origin main --force` (use with caution)

