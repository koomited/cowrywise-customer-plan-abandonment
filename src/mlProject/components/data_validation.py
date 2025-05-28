
import pandas as pd
import warnings
import os
from mlProject.entity.config_entity import DataValidationConfig
from mlProject import logger
warnings.filterwarnings("ignore")

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.data_dir)
            all_cols = list(data.columns)
            dict_cols_types = data.dtypes.apply(lambda x: x.name).to_dict()

            all_schema = self.config.all_schema

            
            for col in all_cols:
                if dict_cols_types[col]==all_schema[col]:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

