# AutoML Web Application

A modern web interface for MLJAR AutoML that allows you to train machine learning models through a beautiful, user-friendly interface without writing any code.

## Features

- **📁 File Upload**: Upload CSV datasets with drag-and-drop support
- **⚙️ Configuration**: Easy setup of training parameters (target column, mode, time limits)
- **📊 Real-time Progress**: Live monitoring of training progress
- **🏆 Results Dashboard**: Interactive leaderboard showing model performance
- **🔮 Predictions**: Make predictions on new data using trained models
- **📋 Reports**: Access detailed HTML reports for each model
- **🔒 Local & Secure**: All data stays on your local machine

## Quick Start

### Prerequisites

- Python 3.8 or higher
- All MLJAR AutoML dependencies installed

### Installation

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the web application:**

   ```bash
   # From the main project directory
   python run_web_app.py

   # Or use the convenience scripts
   # Windows:
   start_web_app.bat

   # Unix/Linux/Mac:
   ./start_web_app.sh
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5000`

## Usage Guide

### 1. Upload Your Dataset

- Click "Choose CSV File" to select your dataset
- The app will display file information (rows, columns, column names)
- Supported format: CSV files only

### 2. Configure Training

- **Target Column**: Select which column contains your target variable
- **Mode**: Choose from:
  - `Explain`: Fast training for data understanding
  - `Perform`: Balanced training for good performance
  - `Compete`: Comprehensive training for best results
  - `Optuna`: Advanced hyperparameter optimization
- **Time Limit**: Set maximum training time in seconds

### 3. Start Training

- Click "Start Training" to begin the AutoML process
- Monitor progress with the real-time progress bar
- Training runs in the background, so you can close the browser if needed

### 4. View Results

- Once training completes, view the model leaderboard
- Click "View Full Report" to see detailed model analysis
- Use "Make Predictions" to test your models on new data

### 5. Make Predictions

- Enter new data in JSON format
- Example:
  ```json
  [
    { "feature1": "value1", "feature2": "value2" },
    { "feature1": "value3", "feature2": "value4" }
  ]
  ```
- Get predictions for all trained models

## API Endpoints

The web app also provides a REST API for programmatic access:

- `POST /api/upload` - Upload CSV file
- `POST /api/train` - Start AutoML training
- `GET /api/status/{session_id}` - Check training status
- `GET /api/results/{session_id}` - Get training results
- `POST /api/predict` - Make predictions


## Example Usage

See `example_usage.py` for a complete example of using the web app programmatically.

## File Structure

```
web_app/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── app.js        # Frontend JavaScript
├── uploads/              # Uploaded files (created automatically)
├── results/              # Training results (created automatically)
└── README.md            # This file
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` (line 200)
2. **File upload fails**: Check file size (max 16MB) and format (CSV only)
3. **Training fails**: Ensure your target column is properly selected
4. **Memory issues**: Reduce dataset size or training time limit

### Logs

Check the console output for detailed error messages and training progress.

## Security Notes

- All data is processed locally on your machine
- No data is sent to external servers
- Uploaded files are stored temporarily in the `uploads/` directory
- Results are stored in the `results/` directory

## Contributing

To contribute to the web application:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This web application is part of the MLJAR AutoML project and follows the same MIT license.




