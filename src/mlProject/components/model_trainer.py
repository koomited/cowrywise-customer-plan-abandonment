
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier  # or any other model
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.linear_model import LogisticRegression
import joblib
from xgboost import XGBClassifier
import pandas as pd
from mlProject.entity.config_entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    def array_to_str_keyed_dict_list(self, X):
        """
        Converts a 2D array into a list of dictionaries
        where keys are string representations of column indices.
        """
        return [dict(zip(map(str, range(X.shape[1])), row)) for row in X]

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        
        # gender_id , and type as categorical variables
        categorical_cols = ["gender_id", "type"]
        train_x[categorical_cols] = train_x[categorical_cols].astype(str)
        
        numeric_cols = train_x.select_dtypes(include=["int64", "float64"]).columns.tolist()
        
        # Step 3: ColumnTransformer for imputing
        preprocessor = ColumnTransformer(transformers=[
            ("num", SimpleImputer(strategy="median"), numeric_cols),
            ("scaler", StandardScaler(), numeric_cols),
            ("cat", SimpleImputer(strategy="most_frequent"), categorical_cols)
        ], remainder="passthrough")  # Keep other columns (if any)

        pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("to_dict", FunctionTransformer(self.array_to_str_keyed_dict_list)),
            ("vectorize", DictVectorizer()),
            ('classifier', XGBClassifier(**self.config.model_params, random_state=42))
        ])

        
        pipeline.fit(train_x, train_y)

        joblib.dump(pipeline, os.path.join(self.config.root_dir, self.config.model_name))

