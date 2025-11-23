// dashboard.js - Dashboard page functionality

// Load API base URL from config.js (loaded before this script)
const API_BASE_URL = window.API_BASE_URL || 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', function() {
    // Check authentication
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    // Load coins
    loadCoins();

    // Setup logout button
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            window.location.href = 'index.html';
        });
    }

    // Setup modal
    setupModal();
});

async function loadCoins() {
    try {
        const response = await fetch(`${API_BASE_URL}/coins`);
        const data = await response.json();
        
        const coinsGrid = document.getElementById('coinsGrid');
        if (coinsGrid && data.coins) {
            coinsGrid.innerHTML = '';
            
            data.coins.forEach(coin => {
                const coinCard = createCoinCard(coin);
                coinsGrid.appendChild(coinCard);
            });
        }
    } catch (error) {
        console.error('Error loading coins:', error);
        const coinsGrid = document.getElementById('coinsGrid');
        if (coinsGrid) {
            coinsGrid.innerHTML = '<p>Error loading coins. Make sure the backend is running.</p>';
        }
    }
}

function createCoinCard(coin) {
    const card = document.createElement('div');
    card.className = 'coin-card';
    card.onclick = () => showCoinHistory(coin.symbol);
    
    const changeClass = coin.change_24h >= 0 ? 'positive' : 'negative';
    const changeSign = coin.change_24h >= 0 ? '+' : '';
    
    card.innerHTML = `
        <h3>${coin.name}</h3>
        <div class="symbol">${coin.symbol}</div>
        <div class="price">$${coin.price.toLocaleString()}</div>
        <div class="change ${changeClass}">${changeSign}${coin.change_24h.toFixed(2)}%</div>
    `;
    
    return card;
}

async function showCoinHistory(coinSymbol) {
    try {
        const response = await fetch(`${API_BASE_URL}/history/${coinSymbol}`);
        const data = await response.json();
        
        const modal = document.getElementById('historyModal');
        const modalCoinName = document.getElementById('modalCoinName');
        const historyChart = document.getElementById('historyChart');
        
        if (modal && modalCoinName && historyChart) {
            modalCoinName.textContent = `${coinSymbol} - Last 30 Days History`;
            
            if (data.history && data.history.length > 0) {
                historyChart.innerHTML = `
                    <table class="predictions-table">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Price</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${data.history.map(item => `
                                <tr>
                                    <td>${item.date || 'N/A'}</td>
                                    <td>$${item.price ? item.price.toLocaleString() : 'N/A'}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                `;
            } else {
                historyChart.innerHTML = '<p>No history data available yet.</p>';
            }
            
            modal.style.display = 'block';
        }
    } catch (error) {
        console.error('Error loading coin history:', error);
        alert('Error loading coin history');
    }
}

function setupModal() {
    const modal = document.getElementById('historyModal');
    const closeBtn = document.querySelector('.close');
    
    if (closeBtn) {
        closeBtn.onclick = function() {
            if (modal) modal.style.display = 'none';
        };
    }
    
    if (modal) {
        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        };
    }
}

