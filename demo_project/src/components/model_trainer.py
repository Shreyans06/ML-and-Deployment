import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor , AdaBoostRegressor , GradientBoostingRegressor

from sklearn.linear_model import LinearRegression , Lasso , Ridge
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object , evaluate_model

@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join('artifacts' , 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self , train_array , test_array):
        try:
            logging.info("Split the data into training and testing")
            X_train  , y_train , X_test , y_test = train_array[:,:-1] , train_array[:,-1] , test_array[:,:-1] , test_array[:,-1]

            models = {
                'Linear Regression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'KNN': KNeighborsRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Random Forest': RandomForestRegressor(),
                'AdaBoost': AdaBoostRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'XGBoost': XGBRegressor(),
                'CatBoost': CatBoostRegressor(verbose=False)
            }

            model_report = evaluate_model(X_train = X_train , y_train = y_train , X_test = X_test , y_test = y_test , models=models)

            # Get the best model name based on R2 score
            best_model_name = max(model_report , key = lambda x : model_report[x]['R2 Score'])

            # Get the best model score
            best_model_score = model_report[best_model_name]['R2 Score']

            if best_model_score < 0.6:
                raise CustomException("Best model score is less than 0.6")

            logging.info(f"Best model is {best_model_name} with R2 Score {best_model_score}")

            save_object(self.model_trainer_config.model_path , models[best_model_name])

            best_model = models[best_model_name]
            predicted = best_model.predict(X_test)
            r2_score_value = r2_score(y_test , predicted)

            return r2_score_value

        except Exception as e:
            raise CustomException(e , sys)