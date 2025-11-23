# 🔧 URGENT FIX: Python Version Issue on Render

## Problem
Render is using Python 3.13, which has compatibility issues with TensorFlow and some packages.

## ✅ SOLUTION: Update Render Service Settings

### Step 1: Go to Your Render Service
1. Go to: https://dashboard.render.com
2. Click on your **`crypto-forecast-api`** service

### Step 2: Change Python Version
1. Click on **"Settings"** tab
2. Scroll down to **"Environment"** section
3. Find **"Python Version"** dropdown
4. Change it to: **`3.11.9`** or **`3.11`**
5. Click **"Save Changes"** at the bottom

### Step 3: Update Build Command
1. Still in Settings, find **"Build Command"**
2. Change it to:
   ```
   pip install --upgrade pip && pip install -r backend/requirements.txt
   ```
3. Click **"Save Changes"**

### Step 4: Redeploy
1. Go to **"Manual Deploy"** tab
2. Click **"Deploy latest commit"**
3. Wait for deployment (3-5 minutes)

## Alternative: Use Minimal Requirements (Faster)

If you want to deploy without ML features first:

1. In Render Settings, change **Build Command** to:
   ```
   pip install --upgrade pip && pip install -r backend/requirements-minimal.txt
   ```
2. Save and redeploy
3. This will deploy the API without TensorFlow (predictions won't work, but everything else will)

## What I've Done

✅ Created `runtime.txt` (Python 3.11.9)
✅ Updated `requirements.txt` (removed TensorFlow temporarily)
✅ Created `requirements-minimal.txt` (for quick deployment)
✅ Pushed fixes to GitHub

## Next Steps

1. **Update Python version in Render dashboard** (most important!)
2. **Redeploy** your service
3. **Test** the deployment

After the basic API works, we can add TensorFlow back later if needed.

