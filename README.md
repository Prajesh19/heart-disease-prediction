# Heart Disease Prediction Web Application

A machine learning web application that predicts the risk of heart disease based on patient health parameters using Logistic Regression.

## Features

- 🎯 Accurate heart disease prediction using trained ML model
- 🌐 Beautiful and responsive web interface
- 📊 Real-time probability calculation
- 💻 Easy-to-use form-based input system

## Project Structure

```
Heart Disease Prediction/
├── app.py                 # Flask web application
├── model/
│   ├── trainmodel.py     # Model training script
│   ├── heart_model.pkl   # Trained model
│   ├── scaler.pkl        # Feature scaler
│   └── ...
├── templates/
│   └── index.html        # Web interface template
├── static/
│   └── style.css         # Styling
├── dataset/
│   └── heart.csv         # Training dataset
└── requirements.txt      # Python dependencies
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model (if not already done)

If you haven't trained the model yet, run:

```bash
python model/trainmodel.py
```

This will create the necessary model files (`heart_model.pkl` and `scaler.pkl`) in the `model/` directory.

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 4. Access the Web Interface

Open your web browser and navigate to:
```
http://localhost:5000
```

## Input Parameters

The application requires the following 13 health parameters:

1. **Age** - Patient's age
2. **Sex** - Gender (Male/Female)
3. **Chest Pain Type** - Type of chest pain (0-3)
4. **Resting Blood Pressure** - Blood pressure in mm Hg
5. **Serum Cholesterol** - Cholesterol level in mg/dl
6. **Fasting Blood Sugar** - Whether fasting blood sugar > 120 mg/dl
7. **Resting ECG Results** - ECG results (0-2)
8. **Max Heart Rate** - Maximum heart rate achieved
9. **Exercise Induced Angina** - Whether angina was induced by exercise
10. **ST Depression (Oldpeak)** - ST depression value
11. **Slope** - Slope of peak exercise ST segment (0-2)
12. **Number of Major Vessels** - Number of major vessels (0-3)
13. **Thalassemia** - Thalassemia type (0-3)

## How It Works

1. User enters patient health parameters through the web form
2. The application scales the input features using the saved scaler
3. The trained Logistic Regression model makes a prediction
4. Results are displayed showing:
   - Prediction (Heart Disease Detected / No Heart Disease Detected)
   - Probability percentage

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (Logistic Regression)
- **Data Processing**: pandas, numpy
- **Frontend**: HTML, CSS, JavaScript

## Notes

- Make sure the model files (`heart_model.pkl` and `scaler.pkl`) exist in the `model/` directory before running the app
- The application runs in debug mode by default for development
- For production, set `debug=False` in `app.py`

## License

This project is for educational purposes.

