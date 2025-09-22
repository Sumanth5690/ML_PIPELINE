from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
import json
import tempfile
import uuid
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store active training sessions
active_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and file.filename.lower().endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Read CSV to get basic info
            df = pd.read_csv(filepath)
            info = {
                'filename': filename,
                'rows': len(df),
                'columns': len(df.columns),
                'column_names': df.columns.tolist(),
                'filepath': filepath
            }
            
            return jsonify({'success': True, 'data': info})
        else:
            return jsonify({'error': 'Please upload a CSV file'}), 400
            
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/train', methods=['POST'])
def train_model():
    try:
        data = request.get_json()
        filepath = data.get('filepath')
        target_column = data.get('target_column')
        mode = data.get('mode', 'Explain')
        time_limit = int(data.get('time_limit', 3600))
        
        if not filepath or not target_column:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Generate unique session ID
        session_id = str(uuid.uuid4())
        results_path = os.path.join(app.config['RESULTS_FOLDER'], session_id)
        
        # Read data
        df = pd.read_csv(filepath)
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Store session info
        active_sessions[session_id] = {
            'status': 'training',
            'results_path': results_path,
            'X': X,
            'y': y,
            'target_column': target_column
        }
        
        # Simulate training process
        import threading
        def train():
            try:
                # Simulate training time
                import time
                time.sleep(2)
                
                # Create mock results
                leaderboard_data = [
                    {'name': 'Baseline', 'score': 0.75, 'time': 0.1},
                    {'name': 'Linear Regression', 'score': 0.82, 'time': 0.5},
                    {'name': 'Random Forest', 'score': 0.88, 'time': 2.1},
                    {'name': 'XGBoost', 'score': 0.91, 'time': 1.8},
                    {'name': 'Ensemble', 'score': 0.93, 'time': 0.3}
                ]
                
                # Save mock leaderboard
                os.makedirs(results_path, exist_ok=True)
                leaderboard_df = pd.DataFrame(leaderboard_data)
                leaderboard_df.to_csv(os.path.join(results_path, 'leaderboard.csv'), index=False)
                
                active_sessions[session_id]['status'] = 'completed'
                active_sessions[session_id]['leaderboard'] = leaderboard_data
                
                logger.info(f"Mock training completed for session {session_id}")
                    
            except Exception as e:
                active_sessions[session_id]['status'] = 'error'
                active_sessions[session_id]['error'] = str(e)
                logger.error(f"Training error: {str(e)}")
        
        thread = threading.Thread(target=train)
        thread.start()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'message': 'Training started (Demo Mode)'
        })
        
    except Exception as e:
        logger.error(f"Training error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<session_id>')
def get_status(session_id):
    if session_id not in active_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = active_sessions[session_id]
    status = {
        'status': session['status'],
        'results_path': session['results_path']
    }
    
    if session['status'] == 'error':
        status['error'] = session.get('error', 'Unknown error')
    
    return jsonify(status)

@app.route('/api/results/<session_id>')
def get_results(session_id):
    if session_id not in active_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = active_sessions[session_id]
    if session['status'] != 'completed':
        return jsonify({'error': 'Training not completed'}), 400
    
    try:
        results_path = session['results_path']
        
        # Read leaderboard
        leaderboard_path = os.path.join(results_path, 'leaderboard.csv')
        if os.path.exists(leaderboard_path):
            df_leaderboard = pd.read_csv(leaderboard_path)
            leaderboard = []
            for idx, row in df_leaderboard.iterrows():
                model_data = {
                    'name': row.get('name', f'Model_{idx+1}'),
                    'score': float(row.get('score', 0)),
                    'time': float(row.get('time', 0))
                }
                leaderboard.append(model_data)
        else:
            leaderboard = session.get('leaderboard', [])
        
        return jsonify({
            'success': True,
            'leaderboard': leaderboard,
            'progress': {'status': 'completed'},
            'results_path': results_path
        })
        
    except Exception as e:
        logger.error(f"Results error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        prediction_data = data.get('data')
        
        if session_id not in active_sessions:
            return jsonify({'error': 'Session not found'}), 404
        
        session = active_sessions[session_id]
        if session['status'] != 'completed':
            return jsonify({'error': 'Training not completed'}), 400
        
        # Mock predictions
        import random
        predictions = []
        for i in range(len(prediction_data)):
            pred = {
                'prediction': random.choice(['Class A', 'Class B', 'Class C']),
                'confidence': round(random.uniform(0.6, 0.95), 3)
            }
            predictions.append(pred)
        
        return jsonify({
            'success': True,
            'predictions': predictions
        })
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    print("Starting MLJAR AutoML Demo Web Application...")
    print("=" * 50)
    print("Web interface will be available at: http://localhost:5000")
    print("This is a DEMO version with limited functionality")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)

