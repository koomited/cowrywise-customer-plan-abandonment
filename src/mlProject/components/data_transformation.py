import os 
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        
        # remove columns with missing values
        data.drop(columns=["address_city", "address_country", "last_transaction_date", "monthly_salary"],
                  inplace=True, errors='ignore')
        # replace NAN values in gender_id column by the most frequent value
        # data["gender_id"] = data["gender_id"].fillna(data["gender_id"].mode()[0])

        # Split the data into training and test sets. (0.75, 0.25) split.
        # create target column
        data["plan_abondonment"] = data["inactivity_days"].apply(
                lambda x: 1 if x >= 365 else 0
            )
        # drop the original inactivity_days column
        data.drop(columns=["inactivity_days"], inplace=True, errors='ignore')            
        train, test = train_test_split(data, 
                                       stratify=data["plan_abondonment"], 
                                       random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)