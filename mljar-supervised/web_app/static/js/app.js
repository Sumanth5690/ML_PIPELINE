// MLJAR AutoML Web Interface JavaScript

class AutoMLApp {
    constructor() {
        this.currentFile = null;
        this.currentSession = null;
        this.pollingInterval = null;
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // File upload
        document.getElementById('fileInput').addEventListener('change', (e) => {
            this.handleFileUpload(e.target.files[0]);
        });

        // Start training
        document.getElementById('startTraining').addEventListener('click', () => {
            this.startTraining();
        });

        // View report
        document.getElementById('viewReport').addEventListener('click', () => {
            this.viewReport();
        });

        // Make prediction
        document.getElementById('makePrediction').addEventListener('click', () => {
            this.showPredictionModal();
        });

        // Run prediction
        document.getElementById('runPrediction').addEventListener('click', () => {
            this.runPrediction();
        });
    }

    async handleFileUpload(file) {
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.success) {
                this.currentFile = result.data;
                this.displayFileInfo(result.data);
                this.populateTargetColumnSelect(result.data.column_names);
                this.showConfigSection();
            } else {
                this.showError(result.error);
            }
        } catch (error) {
            this.showError('Error uploading file: ' + error.message);
        }
    }

    displayFileInfo(fileInfo) {
        const fileInfoDiv = document.getElementById('fileInfo');
        const fileDetails = document.getElementById('fileDetails');
        
        fileDetails.innerHTML = `
            <strong>Filename:</strong> ${fileInfo.filename}<br>
            <strong>Rows:</strong> ${fileInfo.rows.toLocaleString()}<br>
            <strong>Columns:</strong> ${fileInfo.columns}<br>
            <strong>Column Names:</strong> ${fileInfo.column_names.join(', ')}
        `;
        
        fileInfoDiv.style.display = 'block';
    }

    populateTargetColumnSelect(columns) {
        const select = document.getElementById('targetColumn');
        select.innerHTML = '<option value="">Select target column...</option>';
        
        columns.forEach(column => {
            const option = document.createElement('option');
            option.value = column;
            option.textContent = column;
            select.appendChild(option);
        });
    }

    showConfigSection() {
        document.getElementById('configSection').style.display = 'block';
    }

    async startTraining() {
        const targetColumn = document.getElementById('targetColumn').value;
        const mode = document.getElementById('mode').value;
        const timeLimit = document.getElementById('timeLimit').value;

        if (!targetColumn) {
            this.showError('Please select a target column');
            return;
        }

        try {
            const response = await fetch('/api/train', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    filepath: this.currentFile.filepath,
                    target_column: targetColumn,
                    mode: mode,
                    time_limit: timeLimit
                })
            });

            const result = await response.json();

            if (result.success) {
                this.currentSession = result.session_id;
                this.showTrainingSection();
                this.startPolling();
            } else {
                this.showError(result.error);
            }
        } catch (error) {
            this.showError('Error starting training: ' + error.message);
        }
    }

    showTrainingSection() {
        document.getElementById('trainingSection').style.display = 'block';
        document.getElementById('resultsSection').style.display = 'none';
    }

    startPolling() {
        this.pollingInterval = setInterval(() => {
            this.checkTrainingStatus();
        }, 2000);
    }

    stopPolling() {
        if (this.pollingInterval) {
            clearInterval(this.pollingInterval);
            this.pollingInterval = null;
        }
    }

    async checkTrainingStatus() {
        try {
            const response = await fetch(`/api/status/${this.currentSession}`);
            
            // Handle 404 - session doesn't exist (server restarted or session expired)
            if (response.status === 404) {
                this.stopPolling();
                this.showError('Training session expired or not found. Please start a new training session.');
                return;
            }
            
            const result = await response.json();

            if (result.status === 'completed') {
                this.stopPolling();
                this.showResults();
                this.loadResults();
            } else if (result.status === 'error') {
                this.stopPolling();
                this.showError('Training failed: ' + result.error);
            }
            // If still training, continue polling
        } catch (error) {
            console.error('Error checking status:', error);
            // Stop polling on any error to prevent infinite requests
            this.stopPolling();
        }
    }

    showResults() {
        document.getElementById('trainingSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'block';
    }

    async loadResults() {
        try {
            const response = await fetch(`/api/results/${this.currentSession}`);
            const result = await response.json();

            if (result.success) {
                this.displayLeaderboard(result.leaderboard);
            } else {
                this.showError(result.error);
            }
        } catch (error) {
            this.showError('Error loading results: ' + error.message);
        }
    }

    displayLeaderboard(leaderboard) {
        const tbody = document.querySelector('#leaderboardTable tbody');
        tbody.innerHTML = '';

        leaderboard.forEach((model, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${model.name || 'Model'}</td>
                <td>${model.metric_value !== 'N/A' ? model.metric_value.toFixed(4) : 'N/A'}</td>
                <td>${model.train_time !== 'N/A' ? model.train_time.toFixed(2) + 's' : 'N/A'}</td>
            `;
            tbody.appendChild(row);
        });
    }

    viewReport() {
        if (this.currentSession) {
            window.open(`/report?session=${this.currentSession}`, '_blank');
        }
    }

    showPredictionModal() {
        if (!this.currentSession) {
            this.showError('Please complete training first before making predictions');
            return;
        }
        const modal = new bootstrap.Modal(document.getElementById('predictionModal'));
        modal.show();
    }

    async runPrediction() {
        const predictionData = document.getElementById('predictionData').value;
        const resultsDiv = document.getElementById('predictionResults');

        if (!this.currentSession) {
            this.showError('No active session found. Please complete training first.');
            return;
        }

        if (!predictionData.trim()) {
            this.showError('Please enter prediction data');
            return;
        }

        try {
            const data = JSON.parse(predictionData);
            
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    session_id: this.currentSession,
                    data: data
                })
            });

            const result = await response.json();

            if (result.success) {
                this.displayPredictionResults(result.predictions);
            } else {
                this.showError(result.error);
            }
        } catch (error) {
            if (error instanceof SyntaxError) {
                this.showError('Invalid JSON format');
            } else {
                this.showError('Error making prediction: ' + error.message);
            }
        }
    }

    displayPredictionResults(predictions) {
        const resultsDiv = document.getElementById('predictionResults');
        
        let html = '<h6>Prediction Results:</h6>';
        html += '<div class="table-responsive"><table class="table table-striped">';
        html += '<thead><tr>';
        
        // Get column names from first prediction
        if (predictions.length > 0) {
            Object.keys(predictions[0]).forEach(key => {
                html += `<th>${key}</th>`;
            });
        }
        
        html += '</tr></thead><tbody>';
        
        predictions.forEach(prediction => {
            html += '<tr>';
            Object.values(prediction).forEach(value => {
                html += `<td>${typeof value === 'number' ? value.toFixed(4) : value}</td>`;
            });
            html += '</tr>';
        });
        
        html += '</tbody></table></div>';
        
        resultsDiv.innerHTML = html;
    }

    showError(message) {
        // Create a simple alert for now
        alert('Error: ' + message);
    }
}

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new AutoMLApp();
});


