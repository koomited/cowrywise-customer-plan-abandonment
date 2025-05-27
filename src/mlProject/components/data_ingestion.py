import mysql.connector
import pandas as pd
from mlProject.utils.common import get_size
from mlProject import logger
import warnings
import os
from pathlib import Path
from mlProject.entity.config_entity import DataIngestionConfig
warnings.filterwarnings("ignore")

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def connect_to_database(self,
        host: str = "localhost",
        port: str = "3307",
        user: str = "root",
        password: str = "mysecret",
        database: str = "adashi_staging"
    ):
        """
        Establishes and returns a MySQL database connection if successful.

        Args:
            host (str): Database host address.
            port (str): Port number.
            user (str): Database username.
            password (str): Database password.
            database (str): Database name.

        Returns:
            MySQLConnection: A valid MySQL connection object.

        Raises:
            Error: If the connection fails.
        """
        try:
            conn = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if conn.is_connected():
                logger.info("Database connection established successfully.")
                return conn
            else:
                logger.error("Failed to connect to the database.")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")

    def retrieve_data(self):
        connection = self.connect_to_database(
            host=self.config.host,
            port=self.config.port,
            user=self.config.user,
            password=self.config.password,
            database=self.config.database_name
        )
        if not os.path.exists(self.config.local_data_file):
            data = pd.read_sql(self.config.sql_query, connection)
            data.to_csv(self.config.local_data_file, index=False)
            logger.info(f"data fetched with following info: shape:{data.shape}")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))} bytes")
            
        connection.close()
        