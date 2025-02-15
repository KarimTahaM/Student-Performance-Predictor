# Description: This file is the main file that will be run to start the web application.
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import logging
import os

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

application = Flask(__name__)

app = application

# Configure logging
logging.basicConfig(level=logging.INFO)

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

## Route for a prediction page
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  
                writing_score=float(request.form.get('writing_score'))   
                )
            
            pred_df = data.get_data_as_data_frame()
            logging.info(f"Input DataFrame: {pred_df}")
            
            predict_pipeline = PredictPipeline()
            
            # Add more specific error message
            if not os.path.exists("artifacts"):
                return render_template('home.html', 
                    error="Model files not found. Please ensure the model is trained before making predictions.")
            
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results[0])
            
        except CustomException as e:
            logging.error(f"CustomException: {e}")
            return render_template('home.html', 
                error="Model files are missing. Please ensure the model is properly trained.")
        except Exception as e:
            logging.error(f"Unhandled Exception: {e}")
            return render_template('home.html', 
                error="An unexpected error occurred. Please try again later.")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)