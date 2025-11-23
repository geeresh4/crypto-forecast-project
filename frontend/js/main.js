// main.js - Main JavaScript file for index.html

// Check if user is logged in
document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('token');
    if (token) {
        // User is logged in, update navigation
        const navButtons = document.querySelector('.nav-buttons');
        if (navButtons) {
            navButtons.innerHTML = `
                <a href="dashboard.html" class="btn btn-primary">Dashboard</a>
                <a href="prediction.html" class="btn btn-secondary">Predictions</a>
            `;
        }
    }
});

