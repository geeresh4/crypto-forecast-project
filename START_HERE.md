# 🚀 Start Here - Push to GitHub

## ⚡ Quick Steps

### 1. Install Git (5 minutes)

**Download and Install**:
1. Go to: **https://git-scm.com/download/win**
2. Click the big "Download" button
3. Run the installer (Git-2.x.x-64-bit.exe)
4. Click "Next" through all screens (defaults are fine)
5. Click "Install" and wait
6. Click "Finish"

**Verify Installation**:
- Close this window and open a NEW PowerShell window
- Type: `git --version`
- You should see a version number

### 2. Create GitHub Repository (2 minutes)

1. Go to: **https://github.com/new**
2. Repository name: `crypto-forecast-project`
3. Description: "Cryptocurrency price forecasting system"
4. Set to **Public**
5. **DO NOT** check any boxes (no README, no .gitignore, no license)
6. Click **"Create repository"**

### 3. Generate GitHub Token (2 minutes)

1. Go to: **https://github.com/settings/tokens**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name: `Crypto Forecast Push`
4. Select scope: **`repo`** (check the box)
5. Click **"Generate token"**
6. **COPY THE TOKEN** (you won't see it again!)
7. Save it somewhere safe

### 4. Push Code (1 minute)

**Option A: Use Automated Script** (Easiest)
```powershell
.\push_to_github.ps1
```
Follow the prompts!

**Option B: Manual Commands**
Open PowerShell in this folder and run:

```powershell
git init
git add .
git commit -m "Initial commit: Crypto Forecast Project"
git remote add origin https://github.com/geeresh4/crypto-forecast-project.git
git branch -M main
git push -u origin main
```

When asked for credentials:
- **Username**: `geeresh4`
- **Password**: Paste the token you copied (not your GitHub password)

## ✅ Done!

After pushing, visit: **https://github.com/geeresh4/crypto-forecast-project**

You should see all your files!

## 🆘 Need Help?

- **Git not found**: Close and reopen PowerShell after installing Git
- **Authentication failed**: Make sure you're using the token, not password
- **Repository not found**: Make sure you created it on GitHub first

## 📋 Next Step

After pushing to GitHub, deploy to Render:
- See `RENDER_DEPLOYMENT.md` for instructions

