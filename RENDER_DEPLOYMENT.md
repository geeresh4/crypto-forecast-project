# Render Deployment Guide

This guide will help you deploy the Crypto Forecast project to Render.

## Prerequisites

1. **GitHub Repository**: Your code must be pushed to GitHub first
   - Follow `QUICK_START.md` or `GITHUB_SETUP.md` to push to GitHub
   - Repository URL: `https://github.com/geeresh4/crypto-forecast-project`

2. **Render Account**: Sign up at https://render.com (free tier available)

## Deployment Steps

### Step 1: Deploy Backend API

1. **Go to Render Dashboard**: https://dashboard.render.com

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub account if not already connected
   - Select repository: `geeresh4/crypto-forecast-project`

3. **Configure Backend Service**:
   - **Name**: `crypto-forecast-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or choose paid for better performance)

4. **Environment Variables** (Optional):
   - `PYTHON_VERSION`: `3.11.0`
   - `PORT`: `8000` (Render sets this automatically)

5. **Click "Create Web Service"**

6. **Wait for Deployment**:
   - Render will build and deploy your backend
   - Note the URL (e.g., `https://crypto-forecast-api.onrender.com`)

### Step 2: Update Frontend API URL

1. **Update `frontend/js/config.js`**:
   - Replace `'https://crypto-forecast-api.onrender.com'` with your actual Render backend URL
   - Or use the environment detection (already configured)

2. **Commit and Push**:
   ```bash
   git add frontend/js/config.js
   git commit -m "Update API URL for Render deployment"
   git push
   ```

### Step 3: Deploy Frontend

**Option A: Render Static Site (Recommended)**

1. **Create New Static Site**:
   - Click "New +" → "Static Site"
   - Connect GitHub repository: `geeresh4/crypto-forecast-project`

2. **Configure Static Site**:
   - **Name**: `crypto-forecast-frontend`
   - **Build Command**: (leave empty or `echo "No build needed"`)
   - **Publish Directory**: `frontend`
   - **Plan**: Free

3. **Click "Create Static Site"**

**Option B: GitHub Pages (Alternative)**

1. Go to your GitHub repository settings
2. Navigate to "Pages"
3. Source: Deploy from `main` branch, `/frontend` folder
4. Save

### Step 4: Update CORS (if needed)

The backend already has CORS configured to allow all origins. If you need to restrict it:

1. Go to your backend service on Render
2. Add Environment Variable:
   - Key: `ALLOWED_ORIGINS`
   - Value: `https://crypto-forecast-frontend.onrender.com` (your frontend URL)

3. Update `backend/app.py` to use this variable if needed

## Post-Deployment

### 1. Process Historical Data

You can run the data collection script locally and commit the data files, or:

1. SSH into Render (if available on your plan)
2. Or run locally and commit processed data:
   ```bash
   python backend/collect_data.py
   git add backend/data/*.csv
   git commit -m "Add historical data"
   git push
   ```

### 2. Train Models

Models can be trained locally and committed, or you can:
- Use Render's scheduled jobs (paid plans)
- Train locally and commit model files (if small enough)
- Or train on first API call (not recommended for production)

### 3. Test Your Deployment

1. **Backend API**: Visit `https://crypto-forecast-api.onrender.com`
   - Should see: `{"message": "Crypto Forecast API"}`

2. **Frontend**: Visit your frontend URL
   - Should see the home page
   - Test login/register functionality
   - Test coin listing and predictions

## Troubleshooting

### Backend Issues

**Build Fails**:
- Check `backend/requirements.txt` for all dependencies
- Ensure Python version is compatible
- Check build logs in Render dashboard

**App Crashes**:
- Check logs in Render dashboard
- Verify all file paths are correct
- Ensure database directory exists

**CORS Errors**:
- Verify CORS middleware is configured
- Check that frontend URL is allowed

### Frontend Issues

**API Calls Fail**:
- Verify `config.js` has correct backend URL
- Check browser console for errors
- Ensure backend is running and accessible

**Static Files Not Loading**:
- Verify publish directory is `frontend`
- Check file paths are relative (not absolute)

### Common Solutions

1. **Check Render Logs**: Always check the logs in Render dashboard
2. **Verify Environment Variables**: Ensure all required variables are set
3. **Test Locally First**: Make sure everything works locally before deploying
4. **Check File Paths**: Render may have different directory structure

## Render Free Tier Limitations

- **Spins Down After Inactivity**: Free services spin down after 15 minutes of inactivity
- **Cold Start**: First request after spin-down may take 30-60 seconds
- **Build Time**: Limited build minutes per month
- **Bandwidth**: Limited bandwidth

**Solutions**:
- Use paid tier for always-on service
- Set up uptime monitoring to keep service awake
- Optimize build times

## Updating Your Deployment

1. **Make Changes Locally**
2. **Commit and Push to GitHub**:
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```
3. **Render Auto-Deploys**: Render automatically detects changes and redeploys

## Useful Links

- Render Dashboard: https://dashboard.render.com
- Render Docs: https://render.com/docs
- Your Backend: `https://crypto-forecast-api.onrender.com`
- Your Frontend: `https://crypto-forecast-frontend.onrender.com`

## Next Steps

After successful deployment:
1. Test all functionality
2. Monitor logs for any errors
3. Set up custom domain (optional)
4. Configure environment variables for production
5. Set up database (if moving from JSON to SQL)

