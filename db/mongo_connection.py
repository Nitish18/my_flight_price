from pymongo import MongoClient
from app import app

print app.config


def initiate_mongo_connection():
    """
    params : None
    return : mongo connection object
    """
    mongo_client = MongoClient(host=app.config['MONGO_HOST'], port=app.config['MONGO_PORT'], maxPoolSize = 100)
    return mongo_client

def mongo_connection(db = app.config['MONGO_DB']):
	mongo_client = initiate_mongo_connection()
	mongo_db = mongo_client[db]
	return mongo_db