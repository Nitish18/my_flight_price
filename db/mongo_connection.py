from pymongo import MongoClient
import config as config

def initiate_mongo_connection():
    """
    params : None
    return : mongo connection object
    """
    mongo_client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT, maxPoolSize = 100)
    return mongo_client

def mongo_connection(_object, db = config.MONGO_DB):
	mongo_client = initiate_mongo_connection()
	mongo_db = mongo_client[db]
	return mongo_db[_object.__class__.__name__]