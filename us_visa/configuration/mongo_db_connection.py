
import pymongo, os, sys, certifi 
from us_visa.exception import USvisaException
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.logger import logging

# print(DATABASE_NAME)
# print(os.getenv(DATABASE_NAME))


ca = certifi.where()

class MongoDBClient:
    """
    Class Name : export_data_info_feature_store
    Description : This method exports the dataframe from mongodb feature store as dataframe
    Output : Connection to mongodb database
    On Failure: Raises an exception
    """
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.cliente = MongoDBClient.client
            self.database = self.cliente[database_name]
            self.database_name = database_name
            logging.info(f"MongoDB connection succesfull in database {self.database_name}")
        except Exception as e:
            raise USvisaException(e, sys)