from sklearn.metrics import (
    accuracy_score,
    roc_auc_score
)

import os
import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
from urllib.parse import urlparse
from mlProject.utils.common import save_json, create_directories
from pathlib import Path
from mlProject.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self, model,  X_text, y_test):
        preds = model.predict(X_text)
        predict_probs = model.predict_proba(X_text)[:, 1]
        accuracy = accuracy_score(y_test, preds)
        roc_auc = roc_auc_score(y_test, predict_probs)
        
        return accuracy, roc_auc
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]
        categorical_cols = ["gender_id", "type"]
        
        X_test[categorical_cols] = X_test[categorical_cols].astype(str)
        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():


            (accuracy, roc_auc) = self.eval_metrics(model,  X_test, y_test)
            
            # Saving metrics as local
            scores = {"accuracy": accuracy, "roc_auc": roc_auc}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("roc_auc", roc_auc)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="XGBoostModel")
            else:
                mlflow.sklearn.log_model(model, "model")

    