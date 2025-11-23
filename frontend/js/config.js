// config.js - API configuration for different environments

// ============================================
// CONFIGURE YOUR BACKEND URL HERE
// ============================================
// Replace 'YOUR_BACKEND_URL' below with your actual Render backend URL
// Example: 'https://crypto-forecast-api.onrender.com'
const BACKEND_URL = 'YOUR_BACKEND_URL'; // ⬅️ UPDATE THIS!

// ============================================
// Auto-detection (only works if frontend is on same domain)
// ============================================
function getApiBaseUrl() {
    // If manually configured, use that
    if (BACKEND_URL && BACKEND_URL !== 'YOUR_BACKEND_URL') {
        return BACKEND_URL;
    }
    
    // Check if we're on Render (production)
    if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
        // Production: Try to detect Render backend URL
        const hostname = window.location.hostname;
        if (hostname.includes('onrender.com')) {
            // Replace frontend service name with backend service name
            const backendUrl = hostname.replace('crypto-forecast-frontend', 'crypto-forecast-api');
            return `https://${backendUrl}`;
        }
        // Fallback: Return empty to show error
        return '';
    }
    // Development: Use localhost
    return 'http://localhost:8000';
}

// Set global API_BASE_URL
const API_BASE_URL = getApiBaseUrl();

// Validate configuration
if (!API_BASE_URL || API_BASE_URL === 'YOUR_BACKEND_URL') {
    console.error('⚠️ BACKEND URL NOT CONFIGURED!');
    console.error('Please update frontend/js/config.js with your Render backend URL');
    console.error('Example: https://crypto-forecast-api.onrender.com');
}

window.API_BASE_URL = API_BASE_URL;
