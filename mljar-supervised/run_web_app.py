#!/usr/bin/env python3
"""
MLJAR AutoML Web Application Launcher

This script starts the local web interface for MLJAR AutoML.
Run this script to launch the web application.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    web_app_dir = script_dir / "web_app"
    
    # Change to the web_app directory
    os.chdir(web_app_dir)
    
    # Add the parent directory to Python path so supervised module can be imported
    parent_dir = str(script_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    print("Starting MLJAR AutoML Web Application...")
    print("=" * 50)
    print("Web interface will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Import and run the Flask app
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

if __name__ == "__main__":
    main()


