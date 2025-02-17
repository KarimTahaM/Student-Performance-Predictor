# Student Performance Predictor

## Project Overview
This project implements a machine learning system to predict student mathematics scores based on various demographic and academic factors. The system uses a Flask web interface for easy interaction and provides real-time predictions using trained ML models.

## Features
- Predicts mathematics scores based on:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score
- Web-based interface for easy interaction
- Supports multiple ML models with automated model selection
- Comprehensive error handling and logging

## Installation & Setup
1. Clone the repository
```bash
git clone https://github.com/KarimTahaM/Student-Performance-Predictor
cd Student-Performance-Predictor
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Train the model (if not already trained):
```bash
python src/components/data_ingestion.py
```

2. Run the Flask application:
```bash
python app.py
```

3. Open web browser and navigate to:
```
http://localhost:5000
```

## Model Training
The system evaluates multiple models including:
- Random Forest
- Decision Tree
- XGBoost
- CatBoost
- AdaBoost
- Gradient Boosting
- Linear Regression
- K-Neighbors Regressor

The best performing model is automatically selected and saved for predictions.

## Technologies Used
- Python 3.x
- scikit-learn
- Flask
- Pandas
- NumPy
- XGBoost
- CatBoost

## Contributing
Feel free to submit issues, fork the repository and create pull requests for any improvements.
