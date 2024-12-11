<a id="readme-top"></a>

# Credit Card Risk Classification for Applicant Evaluation

A web-based application that predicts credit card approval risk using machine learning model.

Class of  RSBP C

| Name | NRP |
|------|------|
|Nathaniel Ryo Kurniadi|5025221019|
|Mikha Gracia Sugiono | 5025221037|
|Moch. Avin| 5025221061|
|Azarel Grahandito Adi | 5025221126
|Muhammad Nabil Fadhil | 5025221200|

## About this Project

This application is designed to help financial institutions assess credit card applications by predicting the risk level of potential customers. Built using Flask and CatBoost machine learning model, it provides real-time risk assessment based on various applicant parameters.

Key Features:
- Interactive web interface for data input
- Real-time risk prediction using CatBoost model
- Comprehensive applicant assessment
- Responsive design for all devices
- Docker support for easy deployment
- Secure and efficient data processing

Technologies Used:
- Python/Flask for backend
- CatBoost ML Model for predictions
- HTML/CSS/JavaScript for frontend
- Docker for containerization
- Pandas/NumPy for data processing

<p align="right">(<a href="#readme-top">Back to Top</a>)</p>

## How it works

### Input Parameters
The application processes the following input parameters:

1. Personal Information
    - Gender (Male/Female)
    - Car Ownership Status
    - Real Estate Ownership
    - Number of Children

2. Contact & Education
    - Education Level (4 categories)
    - Phone Ownership (Work/Personal)
    - Email Status

3. Financial & Employment
    - Income Level (3 ranges)
    - Years of Employment
    - Employment Status
    - Occupation Type
    - Family Member Count

### Risk Assessment Process

1. Data Collection & Validation
    - Web form captures user inputs
    - Input validation ensures data quality
    - Data preprocessing for model compatibility

2. Model Processing
    - CatBoost model evaluates risk factors
    - Real-time prediction generation
    - Binary classification (High Risk/Low Risk)

### Prerequisites

Before you begin, ensure you have:
- Python 3 or higher installed
- Docker (if using containerized deployment)
- A modern web browser
- Active internet connection

## Installation Guide

### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/NathanielRN/CreditCardApprovalPrediction.git
cd CreditCardApprovalPrediction
```

2. Build and run with Docker:
```bash
docker build -t credit-risk-app .
docker run -p 5000:5000 credit-risk-app
```

3. Access the application at `http://localhost:5000`

### Option 2: Manual Setup

1. Clone the repository:
```bash
git clone https://github.com/NathanielRN/CreditCardApprovalPrediction.git

cd CreditCardApprovalPrediction
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment

# For Windows:
venv\Scripts\activate
# For Unix/MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
flask run
```

5. Access the application at `http://localhost:5000`