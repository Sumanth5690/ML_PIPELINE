from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import os
import json
from supervised.automl import AutoML
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

@app.route('/report')
def report():
    return render_template('report.html')

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
        
        # Initialize AutoML
        automl = AutoML(
            results_path=results_path,
            total_time_limit=time_limit,
            mode=mode,
            train_ensemble=True
        )
        
        # Store session info
        active_sessions[session_id] = {
            'status': 'training',
            'results_path': results_path,
            'automl': automl,
            'X': X,
            'y': y
        }
        
        # Start training in background
        import threading
        def train():
            try:
                automl.fit(X, y)
                active_sessions[session_id]['status'] = 'completed'
                active_sessions[session_id]['automl'] = automl
                
                # Generate HTML report
                try:
                    report_html = automl._report()
                    logger.info(f"Report generated for session {session_id}")
                except Exception as report_error:
                    logger.warning(f"Could not generate report: {str(report_error)}")
                    
            except Exception as e:
                active_sessions[session_id]['status'] = 'error'
                active_sessions[session_id]['error'] = str(e)
                logger.error(f"Training error: {str(e)}")
        
        thread = threading.Thread(target=train)
        thread.start()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'message': 'Training started'
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
    # Handle test_results for demonstration
    if session_id == 'test_results':
        # Get the path to the test_results folder (one level up from web_app)
        # Use current working directory approach since __file__ might not be available
        web_app_dir = os.path.dirname(os.path.abspath(os.getcwd()))
        if 'web_app' in os.getcwd():
            web_app_dir = os.path.dirname(os.getcwd())
        test_results_path = os.path.join(web_app_dir, 'test_results')
        leaderboard_path = os.path.join(test_results_path, 'leaderboard.csv')
        
        if os.path.exists(leaderboard_path):
            import csv
            leaderboard = []
            with open(leaderboard_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    leaderboard.append({
                        'name': row['name'],
                        'model_type': row['model_type'],
                        'metric_type': row.get('metric_type', 'N/A'),
                        'metric_value': float(row['metric_value']),
                        'train_time': float(row['train_time'])
                    })
            
            # Sort leaderboard by metric_value (score) - lower is better for most metrics like logloss
            leaderboard.sort(key=lambda x: x['metric_value'])
            return jsonify({'success': True, 'leaderboard': leaderboard})
        else:
            return jsonify({'success': False, 'error': 'Test results not found'})
    
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
            logger.info(f"Leaderboard columns: {df_leaderboard.columns.tolist()}")
            logger.info(f"Leaderboard data: {df_leaderboard.head()}")
            
            # Format the leaderboard data properly
            leaderboard = []
            for idx, row in df_leaderboard.iterrows():
                # Try different possible column names for score and time
                score_value = None
                time_value = None
                
                # Use the correct column names from MLJAR leaderboard
                if 'metric_value' in row and pd.notna(row['metric_value']):
                    score_value = row['metric_value']
                
                if 'train_time' in row and pd.notna(row['train_time']):
                    time_value = row['train_time']
                
                model_data = {
                    'name': row.get('name', f'Model_{idx+1}'),
                    'model_type': row.get('model_type', 'N/A'),
                    'metric_value': score_value if score_value is not None else 'N/A',
                    'train_time': time_value if time_value is not None else 'N/A'
                }
                
                # Convert metric_value to float if possible
                try:
                    if model_data['metric_value'] != 'N/A':
                        model_data['metric_value'] = float(model_data['metric_value'])
                except (ValueError, TypeError):
                    model_data['metric_value'] = 'N/A'
                
                # Convert train_time to float if possible
                try:
                    if model_data['train_time'] != 'N/A':
                        model_data['train_time'] = float(model_data['train_time'])
                except (ValueError, TypeError):
                    model_data['train_time'] = 'N/A'
                
                leaderboard.append(model_data)
            
            # Sort leaderboard by metric_value (score) - lower is better for most metrics like logloss
            # Put models with 'N/A' scores at the end
            leaderboard.sort(key=lambda x: (x['metric_value'] == 'N/A', x['metric_value'] if x['metric_value'] != 'N/A' else float('inf')))
        else:
            leaderboard = []
        
        # Read progress
        progress_path = os.path.join(results_path, 'progress.json')
        if os.path.exists(progress_path):
            with open(progress_path, 'r') as f:
                progress = json.load(f)
        else:
            progress = {}
        
        return jsonify({
            'success': True,
            'leaderboard': leaderboard,
            'progress': progress,
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
        
        if not session_id:
            return jsonify({'error': 'Session ID is required'}), 400
        
        if session_id not in active_sessions:
            return jsonify({'error': 'Session not found'}), 404
        
        if not prediction_data:
            return jsonify({'error': 'Prediction data is required'}), 400
        
        session = active_sessions[session_id]
        if session['status'] != 'completed':
            return jsonify({'error': 'Training not completed'}), 400
        
        # Convert prediction data to DataFrame
        df = pd.DataFrame(prediction_data)
        
        # Make predictions
        predictions = session['automl'].predict(df)
        
        # Convert numpy array to list of dictionaries
        if hasattr(predictions, 'tolist'):
            # If it's a numpy array, convert to list
            pred_list = predictions.tolist()
        else:
            # If it's already a list or other format
            pred_list = list(predictions)
        
        # Create list of dictionaries with prediction results
        prediction_results = []
        for i, pred in enumerate(pred_list):
            prediction_results.append({
                'row': i + 1,
                'prediction': pred
            })
        
        return jsonify({
            'success': True,
            'predictions': prediction_results
        })
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500



@app.route('/api/params/<session_id>')
def get_params(session_id):
    # Handle test_results for demonstration
    if session_id == 'test_results':
        web_app_dir = os.path.dirname(os.path.abspath(__file__))
        test_results_path = os.path.join(os.path.dirname(web_app_dir), 'test_results')
        params_path = os.path.join(test_results_path, 'params.json')
        if os.path.exists(params_path):
            with open(params_path, 'r') as f:
                params = json.load(f)
            return jsonify({'success': True, 'params': params})
        return jsonify({'success': True, 'params': {}})
    
    if session_id not in active_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = active_sessions[session_id]
    if session['status'] != 'completed':
        return jsonify({'error': 'Training not completed'}), 400
    
    try:
        results_path = session['results_path']
        params_path = os.path.join(results_path, 'params.json')
        
        if os.path.exists(params_path):
            with open(params_path, 'r') as f:
                params = json.load(f)
            return jsonify({'success': True, 'params': params})
        else:
            return jsonify({'success': True, 'params': {}})
            
    except Exception as e:
        logger.error(f"Params error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/data_info/<session_id>')
def get_data_info(session_id):
    # Handle test_results for demonstration
    if session_id == 'test_results':
        web_app_dir = os.path.dirname(os.path.abspath(__file__))
        test_results_path = os.path.join(os.path.dirname(web_app_dir), 'test_results')
        data_info_path = os.path.join(test_results_path, 'data_info.json')
        if os.path.exists(data_info_path):
            with open(data_info_path, 'r') as f:
                data_info = json.load(f)
            return jsonify({'success': True, 'data_info': data_info})
        return jsonify({'success': True, 'data_info': {}})
    
    if session_id not in active_sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    session = active_sessions[session_id]
    if session['status'] != 'completed':
        return jsonify({'error': 'Training not completed'}), 400
    
    try:
        results_path = session['results_path']
        data_info_path = os.path.join(results_path, 'data_info.json')
        
        if os.path.exists(data_info_path):
            with open(data_info_path, 'r') as f:
                data_info = json.load(f)
            return jsonify({'success': True, 'data_info': data_info})
        else:
            return jsonify({'success': True, 'data_info': {}})
            
    except Exception as e:
        logger.error(f"Data info error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/visualization/<session_id>/<path:image_path>')
def get_visualization(session_id, image_path):
    """Serve visualization images for the report"""
    try:
        # Handle test_results for demonstration
        if session_id == 'test_results':
            web_app_dir = os.path.dirname(os.path.abspath(__file__))
            test_results_path = os.path.join(os.path.dirname(web_app_dir), 'test_results')
            full_image_path = os.path.join(test_results_path, image_path)
            
            if os.path.exists(full_image_path) and image_path.endswith('.png'):
                return send_file(full_image_path, mimetype='image/png')
            else:
                return jsonify({'error': 'Image not found'}), 404
        
        # Handle regular session results
        session_path = os.path.join(app.config['RESULTS_FOLDER'], session_id)
        if not os.path.exists(session_path):
            return jsonify({'error': 'Session not found'}), 404
            
        full_image_path = os.path.join(session_path, image_path)
        if os.path.exists(full_image_path) and image_path.endswith('.png'):
            return send_file(full_image_path, mimetype='image/png')
        else:
            return jsonify({'error': 'Image not found'}), 404
            
    except Exception as e:
        logger.error(f"Visualization error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/model_details/<session_id>/<model_name>')
def get_model_details(session_id, model_name):
    """Get detailed information about a specific model"""
    try:
        # Handle test_results for demonstration
        if session_id == 'test_results':
            web_app_dir = os.path.dirname(os.path.abspath(__file__))
            test_results_path = os.path.join(os.path.dirname(web_app_dir), 'test_results')
            model_path = os.path.join(test_results_path, model_name)
        else:
            # Handle regular session results
            session_path = os.path.join(app.config['RESULTS_FOLDER'], session_id)
            if not os.path.exists(session_path):
                return jsonify({'error': 'Session not found'}), 404
            model_path = os.path.join(session_path, model_name)
        
        if not os.path.exists(model_path):
            return jsonify({'error': 'Model not found'}), 404
        
        model_details = {}
        
        # Read framework.json if it exists
        framework_path = os.path.join(model_path, 'framework.json')
        if os.path.exists(framework_path):
            with open(framework_path, 'r') as f:
                model_details['framework'] = json.load(f)
        
        # Read README.md if it exists
        readme_path = os.path.join(model_path, 'README.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                model_details['readme'] = f.read()
        
        # Get list of available visualizations
        visualizations = []
        if os.path.exists(model_path):
            for file in os.listdir(model_path):
                if file.endswith('.png'):
                    visualizations.append(file)
        model_details['visualizations'] = visualizations
        
        # Get feature importance if available
        importance_path = os.path.join(model_path, 'learner_fold_0_importance.csv')
        if os.path.exists(importance_path):
            import pandas as pd
            importance_df = pd.read_csv(importance_path)
            model_details['feature_importance'] = importance_df.to_dict('records')
        
        return jsonify({'success': True, 'model_details': model_details})
        
    except Exception as e:
        logger.error(f"Model details error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

