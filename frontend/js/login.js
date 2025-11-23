// login.js - Login page functionality

// Load API base URL from config.js (loaded before this script)
const API_BASE_URL = window.API_BASE_URL || 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const loginMessage = document.getElementById('loginMessage');

    if (loginForm) {
        loginForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch(`${API_BASE_URL}/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username, password })
                });

                const data = await response.json();

                if (response.ok) {
                    // Store token
                    localStorage.setItem('token', data.token);
                    localStorage.setItem('username', data.username);
                    
                    // Show success message
                    showMessage('Login successful! Redirecting...', 'success');
                    
                    // Redirect to dashboard
                    setTimeout(() => {
                        window.location.href = 'dashboard.html';
                    }, 1500);
                } else {
                    showMessage(data.detail || 'Login failed', 'error');
                }
            } catch (error) {
                showMessage('Error connecting to server. Make sure the backend is running.', 'error');
                console.error('Login error:', error);
            }
        });
    }
});

function clearForm() {
    document.getElementById('loginForm').reset();
    const messageDiv = document.getElementById('loginMessage');
    if (messageDiv) {
        messageDiv.textContent = '';
        messageDiv.className = 'message';
    }
}

function showMessage(message, type) {
    const messageDiv = document.getElementById('loginMessage');
    if (messageDiv) {
        messageDiv.textContent = message;
        messageDiv.className = `message ${type}`;
    }
}

