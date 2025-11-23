// config.js - API configuration for different environments

// Detect if we're running locally or on Render
function getApiBaseUrl() {
    // Check if we're on Render (production)
    if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
        // Production: Try to detect Render backend URL
        // If frontend is on Render, backend is likely on same domain with different subdomain
        const hostname = window.location.hostname;
        if (hostname.includes('onrender.com')) {
            // Replace frontend service name with backend service name
            const backendUrl = hostname.replace('crypto-forecast-frontend', 'crypto-forecast-api');
            return `https://${backendUrl}`;
        }
        // Fallback: Use default Render backend URL (update this with your actual URL)
        return 'https://crypto-forecast-api.onrender.com';
    }
    // Development: Use localhost
    return 'http://localhost:8000';
}

// Set global API_BASE_URL
window.API_BASE_URL = getApiBaseUrl();
const API_BASE_URL = window.API_BASE_URL;

