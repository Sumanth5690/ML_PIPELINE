#!/usr/bin/env python3
"""
Simple script to start the MLJAR AutoML Web Application
"""

import sys
import os
from pathlib import Path

# Add the current directory to Python path so supervised module can be imported
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

print("Starting MLJAR AutoML Web Application...")
print("=" * 50)
print("Web interface will be available at: http://localhost:5000")
print("Press Ctrl+C to stop the server")
print("=" * 50)

try:
    # Change to web_app directory and import the Flask app
    web_app_dir = current_dir / "web_app"
    os.chdir(web_app_dir)
    
    # Add web_app directory to path
    sys.path.insert(0, str(web_app_dir))
    
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)
except ImportError as e:
    print(f"Error: {e}")
    print("\nPlease make sure you have installed all required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except KeyboardInterrupt:
    print("\nShutting down web application...")
    sys.exit(0)
