# PowerShell script to push Crypto Forecast Project to GitHub
# This script will initialize git, commit files, create GitHub repo, and push

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Crypto Forecast - GitHub Push Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "Checking for Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    Write-Host "✓ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "After installing, restart this script." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Repository name
$repoName = "crypto-forecast-project"
$githubUsername = "geeresh4"
$repoUrl = "https://github.com/$githubUsername/$repoName.git"

Write-Host ""
Write-Host "Repository Details:" -ForegroundColor Cyan
Write-Host "  Name: $repoName" -ForegroundColor White
Write-Host "  URL: $repoUrl" -ForegroundColor White
Write-Host ""

# Initialize Git repository
Write-Host "Initializing Git repository..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "✓ Git repository already initialized" -ForegroundColor Green
} else {
    git init
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Failed to initialize Git repository" -ForegroundColor Red
        exit 1
    }
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
}

# Configure Git (if needed)
Write-Host ""
Write-Host "Checking Git configuration..." -ForegroundColor Yellow
$gitUser = git config --global user.name 2>&1
$gitEmail = git config --global user.email 2>&1

if (-not $gitUser -or $gitUser -eq "") {
    Write-Host "Git user name not configured. Please enter your name:" -ForegroundColor Yellow
    $userName = Read-Host "Your name"
    git config --global user.name $userName
}

if (-not $gitEmail -or $gitEmail -eq "") {
    Write-Host "Git email not configured. Please enter your email:" -ForegroundColor Yellow
    $userEmail = Read-Host "Your email"
    git config --global user.email $userEmail
}

# Add all files
Write-Host ""
Write-Host "Adding all files to Git..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to add files" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Files added" -ForegroundColor Green

# Check if there are changes to commit
$status = git status --porcelain
if (-not $status) {
    Write-Host ""
    Write-Host "No changes to commit. Checking if remote is set..." -ForegroundColor Yellow
    
    $remote = git remote get-url origin 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Remote already configured: $remote" -ForegroundColor Green
        Write-Host ""
        Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
        git push -u origin main
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "========================================" -ForegroundColor Green
            Write-Host "✓ Successfully pushed to GitHub!" -ForegroundColor Green
            Write-Host "========================================" -ForegroundColor Green
            Write-Host ""
            Write-Host "Repository URL: $repoUrl" -ForegroundColor Cyan
            exit 0
        }
    }
} else {
    # Create commit
    Write-Host ""
    Write-Host "Creating commit..." -ForegroundColor Yellow
    git commit -m "Initial commit: Crypto Forecast Project - Complete implementation

- Complete folder structure with frontend and backend
- FastAPI backend with authentication, coin listing, history, and prediction endpoints
- LSTM model training scripts
- Data collection from CoinGecko API and CSV processing
- Modern frontend with animated UI
- User authentication system
- Price prediction functionality"
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Failed to create commit" -ForegroundColor Red
        exit 1
    }
    Write-Host "✓ Commit created" -ForegroundColor Green
}

# Check if remote exists
Write-Host ""
Write-Host "Checking remote repository..." -ForegroundColor Yellow
$remoteExists = git remote get-url origin 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Remote already exists: $remoteExists" -ForegroundColor Green
} else {
    Write-Host "Remote not configured. You need to create the repository on GitHub first." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please follow these steps:" -ForegroundColor Cyan
    Write-Host "1. Go to: https://github.com/new" -ForegroundColor White
    Write-Host "2. Repository name: $repoName" -ForegroundColor White
    Write-Host "3. Set to Public (or Private if you prefer)" -ForegroundColor White
    Write-Host "4. DO NOT initialize with README, .gitignore, or license" -ForegroundColor White
    Write-Host "5. Click 'Create repository'" -ForegroundColor White
    Write-Host ""
    
    $continue = Read-Host "Have you created the repository? (y/n)"
    if ($continue -ne "y" -and $continue -ne "Y") {
        Write-Host "Please create the repository and run this script again." -ForegroundColor Yellow
        exit 0
    }
    
    # Add remote
    Write-Host ""
    Write-Host "Adding remote repository..." -ForegroundColor Yellow
    git remote add origin $repoUrl
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Failed to add remote" -ForegroundColor Red
        exit 1
    }
    Write-Host "✓ Remote added" -ForegroundColor Green
}

# Set branch to main
Write-Host ""
Write-Host "Setting branch to main..." -ForegroundColor Yellow
git branch -M main
Write-Host "✓ Branch set to main" -ForegroundColor Green

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "This may prompt for your GitHub credentials." -ForegroundColor Yellow
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ SUCCESS! Code pushed to GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Repository URL: $repoUrl" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "1. Process historical data: python backend/collect_data.py" -ForegroundColor White
    Write-Host "2. Train models: python backend/train_model.py" -ForegroundColor White
    Write-Host "3. Start backend: python backend/app.py" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "✗ Push failed. Common issues:" -ForegroundColor Red
    Write-Host "  - Authentication required (use GitHub Personal Access Token)" -ForegroundColor Yellow
    Write-Host "  - Repository doesn't exist yet" -ForegroundColor Yellow
    Write-Host "  - Network connectivity issues" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For authentication, you may need to:" -ForegroundColor Yellow
    Write-Host "1. Generate a Personal Access Token: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "2. Use it as password when prompted" -ForegroundColor White
    Write-Host ""
}

Read-Host "Press Enter to exit"

