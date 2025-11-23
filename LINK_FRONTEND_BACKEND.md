# 🔗 Link Frontend and Backend - Step by Step

## Step 1: Get Your Backend URL

1. Go to: https://dashboard.render.com
2. Click on your **`crypto-forecast-api`** service
3. **Copy the URL** at the top (e.g., `https://crypto-forecast-api.onrender.com`)

## Step 2: Update Frontend Configuration

1. **Open** `frontend/js/config.js` in your project
2. **Find this line** (around line 7):
   ```javascript
   const BACKEND_URL = 'YOUR_BACKEND_URL'; // ⬅️ UPDATE THIS!
   ```
3. **Replace** `'YOUR_BACKEND_URL'` with your actual backend URL:
   ```javascript
   const BACKEND_URL = 'https://crypto-forecast-api.onrender.com'; // ⬅️ Your actual URL
   ```
4. **Save the file**

## Step 3: Commit and Push

Run these commands in PowerShell:

```powershell
& "C:\Program Files\Git\bin\git.exe" add frontend/js/config.js
& "C:\Program Files\Git\bin\git.exe" commit -m "Update frontend to connect to deployed backend"
& "C:\Program Files\Git\bin\git.exe" push
```

## Step 4: Wait for Frontend Redeploy

1. Render will **automatically redeploy** your frontend (1-2 minutes)
2. Check your frontend URL
3. **Test the connection** - Try logging in or viewing coins

## ✅ Quick Test

After deployment, open your frontend URL and:
1. Open browser console (F12)
2. Check for any errors
3. Try registering a user
4. Try viewing coins

## 🔍 Troubleshooting

### Frontend can't connect to backend?

1. **Check backend URL** - Make sure it's correct in `config.js`
2. **Check backend is running** - Visit backend URL directly (should see `{"message": "Crypto Forecast API"}`)
3. **Check CORS** - Backend already has CORS enabled for all origins
4. **Check browser console** - Look for error messages

### Backend URL format

Make sure your URL:
- ✅ Starts with `https://`
- ✅ Doesn't end with `/`
- ✅ Is the full URL (e.g., `https://crypto-forecast-api.onrender.com`)

### Example Configuration

```javascript
// Correct:
const BACKEND_URL = 'https://crypto-forecast-api.onrender.com';

// Wrong:
const BACKEND_URL = 'crypto-forecast-api.onrender.com';  // Missing https://
const BACKEND_URL = 'https://crypto-forecast-api.onrender.com/';  // Trailing slash
```

## 📝 Alternative: Environment-Based Auto-Detection

The config.js also has auto-detection that works if:
- Frontend is on: `https://crypto-forecast-frontend.onrender.com`
- Backend is on: `https://crypto-forecast-api.onrender.com`

It will automatically detect the backend URL. But manual configuration is more reliable.

## ✅ Done!

Once you update `config.js` and push, your frontend will connect to your backend!

