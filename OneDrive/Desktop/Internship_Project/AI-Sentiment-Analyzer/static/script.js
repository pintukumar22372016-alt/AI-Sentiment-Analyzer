let sentimentChart = null;

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analyze-form');
    const textInput = document.getElementById('text-input');
    const submitBtn = document.getElementById('submit-btn');
    const resultsSection = document.getElementById('results-section');
    
    // Load history on start
    fetchHistory();

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = textInput.value.trim();
        if (!text) return;

        // UI Loading state
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span>Analyzing...</span>';
        submitBtn.disabled = true;
        
        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                displayResults(data);
                fetchHistory(); // Refresh dashboard
            } else {
                alert('Error analyzing text: ' + (data.error || 'Unknown error'));
            }
        } catch (err) {
            console.error(err);
            alert('Failed to connect to the server.');
        } finally {
            submitBtn.innerHTML = originalBtnText;
            submitBtn.disabled = false;
        }
    });
});

function displayResults(data) {
    const resultsSection = document.getElementById('results-section');
    const classEl = document.getElementById('result-classification');
    
    // Show section
    resultsSection.classList.remove('hidden');
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    
    // Update classification text and color class
    classEl.textContent = data.classification;
    classEl.className = `classification ${data.classification}`;
    
    // Animate progress bars
    const pos = (data.scores.pos * 100).toFixed(1);
    const neu = (data.scores.neu * 100).toFixed(1);
    const neg = (data.scores.neg * 100).toFixed(1);
    
    setTimeout(() => {
        document.getElementById('bar-pos').style.width = `${pos}%`;
        document.getElementById('val-pos').textContent = `${pos}%`;
        
        document.getElementById('bar-neu').style.width = `${neu}%`;
        document.getElementById('val-neu').textContent = `${neu}%`;
        
        document.getElementById('bar-neg').style.width = `${neg}%`;
        document.getElementById('val-neg').textContent = `${neg}%`;
    }, 100);
}

async function fetchHistory() {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();
        
        updateDBStatus(data.db_connected);
        
        if (data.chart_data) {
            updateChart(data.chart_data);
        }
        
        if (data.records) {
            updateHistoryList(data.records);
        }
    } catch (err) {
        console.error("Failed to fetch history", err);
        updateDBStatus(false);
    }
}

function updateDBStatus(connected) {
    const badge = document.getElementById('db-status');
    if (connected) {
        badge.textContent = 'Database Online';
        badge.className = 'status-badge online';
    } else {
        badge.textContent = 'Database Offline (No History Saved)';
        badge.className = 'status-badge offline';
    }
}

function updateChart(chartData) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    
    // Set global default color for chart labels in dark mode
    Chart.defaults.color = '#94a3b8';
    
    if (sentimentChart) {
        sentimentChart.destroy();
    }
    
    sentimentChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: chartData.labels,
            datasets: [{
                data: chartData.data,
                backgroundColor: chartData.colors,
                borderWidth: 0,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            family: "'Outfit', sans-serif",
                            size: 14
                        }
                    }
                }
            },
            cutout: '70%'
        }
    });
}

function updateHistoryList(records) {
    const list = document.getElementById('history-list');
    list.innerHTML = ''; // Clear current list
    
    if (records.length === 0) {
        list.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 2rem;">No history found yet. Analyze some text to see it here!</p>';
        return;
    }
    
    records.forEach(record => {
        const date = new Date(record.timestamp).toLocaleString();
        const shortText = record.text.length > 100 ? record.text.substring(0, 100) + '...' : record.text;
        
        const item = document.createElement('div');
        item.className = `history-item ${record.classification}`;
        
        item.innerHTML = `
            <div class="history-text">"${shortText}"</div>
            <div class="history-meta">
                <span>${record.classification} (Compound: ${record.scores.compound})</span>
                <span>${date}</span>
            </div>
        `;
        
        list.appendChild(item);
    });
}
