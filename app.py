import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import catboost

# Load the CatBoost model
model_path = "./catboost_model2.cbm"
model = catboost.CatBoostClassifier()

if os.path.exists(model_path):
    try:
        model.load_model(model_path)
    except catboost.CatBoostError as e:
        print(f"Error loading model: {e}")
else:
    print(f"Model file not found at path: {model_path}")

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict fraud risk.
    Expects JSON input with appropriate feature columns.
    """
    try:
        # Get JSON data from the request
        input_data = request.json
        if not input_data:
            return jsonify({'error': 'No input data provided'}), 400

        # Convert JSON to DataFrame
        df = pd.DataFrame(input_data)

        # Validate input structure
        required_columns = [
            "CODE_GENDER", "FLAG_OWN_CAR", "FLAG_OWN_REALTY", "CNT_CHILDREN",
            "NAME_EDUCATION_TYPE", "FLAG_WORK_PHONE", "FLAG_PHONE", "FLAG_EMAIL",
            "CNT_FAM_MEMBERS", "MONTHS_BALANCE", "INCOME", "EMPLOYMENT_YEARS",
            "EMPLOYMENT_STATUS", "AGE_GROUP", "NAME_INCOME_TYPE_Commercial associate",
            "NAME_INCOME_TYPE_State servant", "NAME_INCOME_TYPE_Working",
            "NAME_FAMILY_STATUS_Civil marriage", "NAME_FAMILY_STATUS_Married",
            "NAME_FAMILY_STATUS_Separated", "NAME_FAMILY_STATUS_Single / not married",
            "NAME_FAMILY_STATUS_Widow", "NAME_HOUSING_TYPE_Co-op apartment",
            "NAME_HOUSING_TYPE_House / apartment", "NAME_HOUSING_TYPE_Municipal apartment",
            "NAME_HOUSING_TYPE_Office apartment", "NAME_HOUSING_TYPE_Rented apartment",
        ]

        # Check if all required columns are present
        missing_columns = [column for column in required_columns if column not in df.columns]
        if missing_columns:
            return jsonify({'error': f'Missing required columns: {", ".join(missing_columns)}'}), 400

        # Check if the model is trained
        if model.is_fitted():
            # Make predictions
            predictions = model.predict(df)
            return jsonify({'predictions': predictions.tolist()})
        else:
            return jsonify({'error': 'Model is not trained. Please train the model before making predictions.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)