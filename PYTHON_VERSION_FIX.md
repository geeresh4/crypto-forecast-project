# 🔧 CRITICAL: Force Python 3.11 in Render Settings

## Problem
Render is using Python 3.13, but Pydantic v1 doesn't support it. The `runtime.txt` file isn't being respected.

## ✅ SOLUTION: Update Render Service Settings

### Step 1: Go to Your Render Service
1. Go to: https://dashboard.render.com
2. Click on your **`crypto-forecast-api`** service

### Step 2: Force Python 3.11
1. Click on **"Settings"** tab
2. Scroll to **"Environment"** section
3. Find **"Python Version"** dropdown
4. **Change it to: `3.11.9`** (or `3.11`)
5. Click **"Save Changes"** at the bottom

### Step 3: Update Build Command
1. Still in Settings, find **"Build Command"**
2. Change it to:
   ```
   pip install --upgrade pip && pip install -r backend/requirements.txt
   ```
3. Click **"Save Changes"**

### Step 4: Manual Deploy
1. Go to **"Manual Deploy"** tab
2. Click **"Deploy latest commit"**
3. Wait for deployment

## Alternative: Use Pydantic v2 (If Python 3.11 doesn't work)

If you can't change Python version, I've updated requirements to use Pydantic v2.6.0 which should have pre-built wheels for Python 3.13.

## ✅ What I've Done

1. ✅ Updated `requirements.txt` to use newer versions
2. ✅ Updated `render.yaml` with Python 3.11.9
3. ✅ Added upgrade pip to build command

## ⚠️ IMPORTANT

**You MUST change Python version to 3.11 in Render dashboard settings!**

The `runtime.txt` file alone isn't enough - Render needs it set in the service settings.

