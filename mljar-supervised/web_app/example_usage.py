#!/usr/bin/env python3
"""
Example usage of the MLJAR AutoML Web Application

This script demonstrates how to use the web application programmatically.
"""

import requests
import json
import time
import pandas as pd
from io import StringIO

# Web app base URL
BASE_URL = "http://localhost:5000"

def test_web_app():
    """Test the web application with a sample dataset"""
    
    print("Testing MLJAR AutoML Web Application")
    print("=" * 50)
    
    # Create sample data
    sample_data = {
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000],
        'education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
        'target': [0, 1, 1, 0, 1]
    }
    
    df = pd.DataFrame(sample_data)
    
    # Save sample data to CSV
    csv_content = df.to_csv(index=False)
    
    print("1. Uploading sample dataset...")
    
    # Upload file
    files = {'file': ('sample_data.csv', csv_content, 'text/csv')}
    response = requests.post(f"{BASE_URL}/api/upload", files=files)
    
    if response.status_code == 200:
        upload_result = response.json()
        print(f"✓ File uploaded successfully: {upload_result['data']['filename']}")
        print(f"  Rows: {upload_result['data']['rows']}, Columns: {upload_result['data']['columns']}")
        
        # Start training
        print("\n2. Starting AutoML training...")
        
        training_data = {
            'filepath': upload_result['data']['filepath'],
            'target_column': 'target',
            'mode': 'Explain',
            'time_limit': 60  # 1 minute for testing
        }
        
        response = requests.post(f"{BASE_URL}/api/train", 
                               headers={'Content-Type': 'application/json'},
                               data=json.dumps(training_data))
        
        if response.status_code == 200:
            train_result = response.json()
            session_id = train_result['session_id']
            print(f"✓ Training started with session ID: {session_id}")
            
            # Poll for completion
            print("\n3. Monitoring training progress...")
            while True:
                response = requests.get(f"{BASE_URL}/api/status/{session_id}")
                if response.status_code == 200:
                    status = response.json()
                    if status['status'] == 'completed':
                        print("✓ Training completed!")
                        break
                    elif status['status'] == 'error':
                        print(f"✗ Training failed: {status.get('error', 'Unknown error')}")
                        return
                    else:
                        print(".", end="", flush=True)
                        time.sleep(2)
                else:
                    print(f"✗ Error checking status: {response.status_code}")
                    return
            
            # Get results
            print("\n4. Retrieving results...")
            response = requests.get(f"{BASE_URL}/api/results/{session_id}")
            
            if response.status_code == 200:
                results = response.json()
                print("✓ Results retrieved successfully!")
                print(f"  Number of models: {len(results['leaderboard'])}")
                
                # Display leaderboard
                if results['leaderboard']:
                    print("\nModel Leaderboard:")
                    print("-" * 50)
                    for i, model in enumerate(results['leaderboard'][:5]):  # Show top 5
                        print(f"{i+1}. {model.get('name', 'Model')} - Score: {model.get('score', 'N/A')}")
                
                # Test prediction
                print("\n5. Testing prediction...")
                prediction_data = [
                    {'age': 28, 'income': 55000, 'education': 'Bachelor'},
                    {'age': 42, 'income': 75000, 'education': 'Master'}
                ]
                
                pred_response = requests.post(f"{BASE_URL}/api/predict",
                                           headers={'Content-Type': 'application/json'},
                                           data=json.dumps({
                                               'session_id': session_id,
                                               'data': prediction_data
                                           }))
                
                if pred_response.status_code == 200:
                    pred_results = pred_response.json()
                    print("✓ Predictions made successfully!")
                    print("Prediction results:")
                    for i, pred in enumerate(pred_results['predictions']):
                        print(f"  Sample {i+1}: {pred}")
                else:
                    print(f"✗ Prediction failed: {pred_response.status_code}")
                
            else:
                print(f"✗ Error retrieving results: {response.status_code}")
        else:
            print(f"✗ Training failed: {response.status_code}")
    else:
        print(f"✗ Upload failed: {response.status_code}")

if __name__ == "__main__":
    try:
        test_web_app()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the web application.")
        print("Make sure the web app is running by executing: python run_web_app.py")
    except Exception as e:
        print(f"Error: {e}")


