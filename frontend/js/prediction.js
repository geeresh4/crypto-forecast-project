// prediction.js - Prediction page functionality

// Load API base URL from config.js (loaded before this script)
const API_BASE_URL = window.API_BASE_URL || 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function() {
    // Check authentication
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    // Load coins for dropdown
    loadCoinsForDropdown();

    // Setup logout button
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            window.location.href = 'index.html';
        });
    }

    // Setup predict button
    const predictBtn = document.getElementById('predictBtn');
    if (predictBtn) {
        predictBtn.addEventListener('click', generatePredictions);
    }
});

async function loadCoinsForDropdown() {
    try {
        const response = await fetch(`${API_BASE_URL}/coins`);
        const data = await response.json();
        
        const coinSelect = document.getElementById('coinSelect');
        if (coinSelect && data.coins) {
            coinSelect.innerHTML = '<option value="">Select a coin</option>';
            
            data.coins.forEach(coin => {
                const option = document.createElement('option');
                option.value = coin.symbol;
                option.textContent = `${coin.name} (${coin.symbol})`;
                coinSelect.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading coins:', error);
    }
}

async function generatePredictions() {
    const coin = document.getElementById('coinSelect').value;
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const country = document.getElementById('country').value;

    if (!coin || !startDate || !endDate) {
        alert('Please fill in all required fields');
        return;
    }

    const predictBtn = document.getElementById('predictBtn');
    const predictionsResult = document.getElementById('predictionsResult');

    // Disable button and show loading
    if (predictBtn) {
        predictBtn.disabled = true;
        predictBtn.textContent = 'Generating Predictions...';
    }

    try {
        const response = await fetch(`${API_BASE_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                coin: coin,
                start: startDate,
                end: endDate
            })
        });

        const data = await response.json();

        if (response.ok && predictionsResult) {
            displayPredictions(data, country);
        } else {
            predictionsResult.innerHTML = `<p class="message error">Error: ${data.detail || 'Failed to generate predictions'}</p>`;
        }
    } catch (error) {
        console.error('Error generating predictions:', error);
        if (predictionsResult) {
            predictionsResult.innerHTML = '<p class="message error">Error connecting to server. Make sure the backend is running.</p>';
        }
    } finally {
        if (predictBtn) {
            predictBtn.disabled = false;
            predictBtn.textContent = 'Generate Predictions';
        }
    }
}

function displayPredictions(data, country) {
    const predictionsResult = document.getElementById('predictionsResult');
    
    if (!predictionsResult) return;

    if (!data.predictions || data.predictions.length === 0) {
        predictionsResult.innerHTML = '<p class="message">No predictions available yet. Model training will be implemented in Phase 2.</p>';
        return;
    }

    let html = `
        <h3>Predictions for ${data.coin}</h3>
        <p><strong>Period:</strong> ${data.start} to ${data.end}</p>
        <table class="predictions-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Predicted Price (USD)</th>
                    ${country ? `<th>Price (${country})</th>` : ''}
                </tr>
            </thead>
            <tbody>
    `;

    data.predictions.forEach(pred => {
        html += `
            <tr>
                <td>${pred.date || 'N/A'}</td>
                <td>$${pred.price ? pred.price.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) : 'N/A'}</td>
                ${country ? `<td>${pred.converted_price || 'N/A'}</td>` : ''}
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
    `;

    predictionsResult.innerHTML = html;
}

