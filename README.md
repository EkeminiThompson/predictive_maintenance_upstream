# Predictive Maintenance Analytics for Upstream Sector Equipment: Flask Application

## Overview

This Flask application demonstrates predictive maintenance analytics tailored for equipment in the upstream sector. Using machine learning, users can input sensor data to predict equipment health and visualize historical trends through interactive charts.

## Key Features

- **User-Friendly Interface:** Input temperature, pressure, and vibration data for predictive analysis.
- **Predictive Modeling:** Utilizes machine learning algorithms to predict equipment status (failure or normal).
- **Real-Time Visualization:** Visualizes historical temperature trends with interactive Chart.js.

## Installation and Setup

### Prerequisites

- Python (3.6 or higher)
- pip (Python package installer)
- Git (optional for cloning repository)

### Clone the Repository

```bash
git clone https://github.com/yourusername/predictive-maintenance-flask.git
cd predictive-maintenance-flask
```

### Install Dependencies

Create a virtual environment and install required packages:

```bash
python -m venv venv
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt
```

### Running the Application

Set Flask app environment variable and start the application:

```bash
export FLASK_APP=app.py
flask run
```

Open [http://localhost:5000](http://localhost:5000) in your browser to access the application.

## Usage

1. **Input Form:**
   - Enter temperature, pressure, and vibration data.
   - Click "Predict" to analyze and view equipment health status.

2. **Prediction Results:**
   - Displays predicted equipment status (failure or normal) and probability.

3. **Historical Data Visualization:**
   - Interactive chart shows historical temperature trends over time.

## Project Structure

```
predictive-maintenance-flask/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # CSS styles
└── templates/
    └── index.html          # HTML template
```

## Technologies Used

- Flask: Web framework for Python
- Chart.js: JavaScript library for data visualization
- Pandas, NumPy, scikit-learn: Libraries for data manipulation and machine learning

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Example data and code snippets used in developing this application.

---

