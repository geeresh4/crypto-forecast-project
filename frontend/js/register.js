// register.js - Registration page functionality

// Load API base URL from config.js (loaded before this script)
const API_BASE_URL = window.API_BASE_URL || 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const registerMessage = document.getElementById('registerMessage');

    if (registerForm) {
        registerForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const country = document.getElementById('country').value;

            // Basic validation
            if (!email || !username || !password || !country) {
                showMessage('Please fill in all fields', 'error');
                return;
            }

            try {
                const response = await fetch(`${API_BASE_URL}/register`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, username, password, country })
                });

                const data = await response.json();

                if (response.ok) {
                    showMessage('Registration successful! Redirecting to login...', 'success');
                    
                    // Redirect to login page
                    setTimeout(() => {
                        window.location.href = 'login.html';
                    }, 1500);
                } else {
                    showMessage(data.detail || 'Registration failed', 'error');
                }
            } catch (error) {
                showMessage('Error connecting to server. Make sure the backend is running.', 'error');
                console.error('Registration error:', error);
            }
        });
    }
});

function clearForm() {
    document.getElementById('registerForm').reset();
    const messageDiv = document.getElementById('registerMessage');
    if (messageDiv) {
        messageDiv.textContent = '';
        messageDiv.className = 'message';
    }
}

function showMessage(message, type) {
    const messageDiv = document.getElementById('registerMessage');
    if (messageDiv) {
        messageDiv.textContent = message;
        messageDiv.className = `message ${type}`;
    }
}

