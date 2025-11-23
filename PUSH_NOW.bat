@echo off
echo ========================================
echo Crypto Forecast - Push to GitHub
echo ========================================
echo.

echo Step 1: Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to: https://git-scm.com/download/win
    echo 2. Download and install Git
    echo 3. Close and reopen this window
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed!
echo.

echo Step 2: Initializing Git repository...
if exist .git (
    echo [OK] Git repository already exists
) else (
    git init
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to initialize Git
        pause
        exit /b 1
    )
    echo [OK] Git repository initialized
)
echo.

echo Step 3: Adding all files...
git add .
if %errorlevel% neq 0 (
    echo [ERROR] Failed to add files
    pause
    exit /b 1
)
echo [OK] Files added
echo.

echo Step 4: Creating commit...
git commit -m "Initial commit: Crypto Forecast Project - Complete implementation" >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] No changes to commit or commit failed
    echo This is OK if you already committed before
) else (
    echo [OK] Commit created
)
echo.

echo Step 5: Checking remote repository...
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo IMPORTANT: Create GitHub Repository First!
    echo ========================================
    echo.
    echo 1. Go to: https://github.com/new
    echo 2. Repository name: crypto-forecast-project
    echo 3. Set to Public
    echo 4. DO NOT check any boxes
    echo 5. Click Create repository
    echo.
    set /p continue="Have you created the repository? (y/n): "
    if /i not "%continue%"=="y" (
        echo Please create the repository and run this script again.
        pause
        exit /b 0
    )
    echo.
    echo Adding remote repository...
    git remote add origin https://github.com/geeresh4/crypto-forecast-project.git
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to add remote
        pause
        exit /b 1
    )
    echo [OK] Remote added
) else (
    echo [OK] Remote already configured
)
echo.

echo Step 6: Setting branch to main...
git branch -M main
echo [OK] Branch set to main
echo.

echo ========================================
echo Step 7: Pushing to GitHub
echo ========================================
echo.
echo You will be prompted for credentials:
echo   Username: geeresh4
echo   Password: Use a Personal Access Token (not your GitHub password)
echo.
echo Generate token: https://github.com/settings/tokens
echo Select scope: repo
echo.
pause

git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo SUCCESS! Code pushed to GitHub!
    echo ========================================
    echo.
    echo Repository: https://github.com/geeresh4/crypto-forecast-project
    echo.
) else (
    echo.
    echo [ERROR] Push failed
    echo.
    echo Common issues:
    echo - Use Personal Access Token as password (not GitHub password)
    echo - Make sure repository exists on GitHub
    echo - Check your internet connection
    echo.
)

pause

