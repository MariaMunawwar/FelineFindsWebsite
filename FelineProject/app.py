from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # <-- Import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)  # <-- Enable CORS on your Flask app

# Load the model
clf = joblib.load("logistic_model.joblib")

# Endpoint for rendering the form
@app.route('/')
def home():
    return render_template('meowmedic.html')

# Endpoint for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Get data from POST request
    new_data = pd.DataFrame([data])  # Convert to DataFrame
    prediction = clf.predict(new_data)  # Make prediction
    return jsonify({"prediction": prediction.tolist()}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)

