import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            logging.info("Training pipeline started")

            # Data Ingestion
            train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed")

            # Data Transformation
            train_arr, test_arr, _ = self.data_transformation.initiate_data_transformation(
                train_data_path, 
                test_data_path
            )
            logging.info("Data transformation completed")

            # Model Training
            best_model_score = self.model_trainer.initiate_model_trainer(
                train_arr, 
                test_arr
            )
            logging.info(f"Model training completed. Best model score: {best_model_score}")

            return best_model_score

        except Exception as e:
            logging.error("Error in training pipeline")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"Error in main: {e}")
        raise CustomException(e, sys)