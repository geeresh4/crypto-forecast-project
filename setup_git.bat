@echo off
echo ========================================
echo Crypto Forecast Project - Git Setup
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH.
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Git is installed!
echo.

echo Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo ERROR: Failed to initialize Git repository
    pause
    exit /b 1
)

echo.
echo Adding all files...
git add .
if %errorlevel% neq 0 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)

echo.
echo Creating initial commit...
git commit -m "Initial commit: Crypto Forecast Project - Complete implementation"
if %errorlevel% neq 0 (
    echo ERROR: Failed to create commit
    pause
    exit /b 1
)

echo.
echo ========================================
echo Git repository initialized and committed!
echo ========================================
echo.
echo Next steps:
echo 1. Create a repository on GitHub at: https://github.com/geeresh4
echo 2. Run the following commands:
echo    git remote add origin https://github.com/geeresh4/REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Replace REPO_NAME with your actual repository name.
echo.
pause

