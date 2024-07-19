import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate mock data
def generate_mock_data(num_samples=1000):
    np.random.seed(42)
    temperature = np.random.uniform(60, 100, num_samples)
    pressure = np.random.uniform(800, 1200, num_samples)
    vibration = np.random.uniform(1, 5, num_samples)
    failure_label = np.random.randint(0, 2, num_samples)  # Binary classification: 0 or 1

    data = pd.DataFrame({
        'temperature': temperature,
        'pressure': pressure,
        'vibration': vibration,
        'failure_label': failure_label
    })

    return data

# Function to train and save the model
def train_and_save_model(data):
    # Separate features and target
    X = data[['temperature', 'pressure', 'vibration']]
    y = data['failure_label']

    # Initialize model (Example: RandomForestClassifier)
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'models/predictive_model.pkl')

# Generate mock data
mock_data = generate_mock_data()

# Train and save the model using mock data
train_and_save_model(mock_data)
