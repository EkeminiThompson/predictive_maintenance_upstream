from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
model = None  # Placeholder for the trained machine learning model

# Load the trained machine learning model
def load_model():
    global model
    model = joblib.load('models/predictive_model.pkl')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to receive sensor data and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        load_model()  # Load the model if not already loaded
    
    # Get data from the POST request
    data = request.form.to_dict()
    
    # Convert the data into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Make predictions
    prediction = model.predict(input_data)
    prediction_prob = model.predict_proba(input_data)[:, 1]  # Probability of failure
    
    # Prepare response
    if prediction[0] == 1:
        result = "Equipment failure predicted."
    else:
        result = "Equipment functioning normally."

    output = {
        "prediction": result,
        "probability": float(prediction_prob[0])
    }

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
