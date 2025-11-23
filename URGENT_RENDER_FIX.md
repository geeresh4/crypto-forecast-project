# 🚨 URGENT: Fix Python Version in Render

## The Problem
Render is using Python 3.13, but your code needs Python 3.11. The `runtime.txt` file isn't being respected.

## ✅ IMMEDIATE FIX (Do This Now!)

### Step 1: Go to Render Dashboard
1. Go to: https://dashboard.render.com
2. Click on your **`crypto-forecast-api`** service

### Step 2: Change Python Version
1. Click **"Settings"** tab
2. Scroll to **"Environment"** section  
3. Find **"Python Version"** dropdown
4. **Select: `3.11.9`** (or just `3.11`)
5. Click **"Save Changes"**

### Step 3: Update Build Command
1. In Settings, find **"Build Command"**
2. Change it to:
   ```
   pip install --upgrade pip && pip install -r backend/requirements.txt
   ```
3. Click **"Save Changes"**

### Step 4: Redeploy
1. Go to **"Manual Deploy"** tab
2. Click **"Deploy latest commit"**
3. Wait 3-5 minutes

## Why This Happened

- Python 3.13 changed `ForwardRef._evaluate()` signature
- Pydantic v1 doesn't support Python 3.13
- Render defaulted to Python 3.13
- `runtime.txt` alone isn't enough - must set in dashboard

## ✅ After Fixing

Your API should start successfully with Python 3.11!

## Alternative (If Python 3.11 doesn't work)

I've also updated requirements to Pydantic v2.6 which has pre-built wheels for Python 3.13. But setting Python 3.11 is the better solution.

