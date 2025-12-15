from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load the trained model and scaler
model_path = 'model/heart_model.pkl'
scaler_path = 'model/scaler.pkl'

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}. Please run trainmodel.py first.")

if not os.path.exists(scaler_path):
    raise FileNotFoundError(f"Scaler file not found: {scaler_path}. Please run trainmodel.py first.")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if all required fields are present
        required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                          'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        
        missing_fields = [field for field in required_fields if field not in request.form or not request.form[field]]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
        
        # Get form data with validation
        try:
            features = [
                int(request.form['age']),
                int(request.form['sex']),
                int(request.form['cp']),
                int(request.form['trestbps']),
                int(request.form['chol']),
                int(request.form['fbs']),
                int(request.form['restecg']),
                int(request.form['thalach']),
                int(request.form['exang']),
                float(request.form['oldpeak']),
                int(request.form['slope']),
                int(request.form['ca']),
                int(request.form['thal'])
            ]
        except (ValueError, KeyError) as e:
            return jsonify({'error': f'Invalid input data: {str(e)}'}), 400
        
        # Validate feature ranges
        if len(features) != 13:
            return jsonify({'error': 'Invalid number of features'}), 400
        
        # Scale the features
        features_scaled = scaler.transform([features])
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        # Get probability of heart disease
        heart_disease_prob = probability[1] * 100
        
        result = {
            'prediction': int(prediction),
            'probability': round(heart_disease_prob, 2),
            'message': 'Heart Disease Detected' if prediction == 1 else 'No Heart Disease Detected'
        }
        
        return jsonify(result)
    
    except KeyError as e:
        return jsonify({'error': f'Missing form field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

if __name__ == '__main__':
    # For production, set debug=False
    # For development, you can set debug=True
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
