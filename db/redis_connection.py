import redis
from app import app
import config as config

def get_redis_connection():
    connection_pool = redis.ConnectionPool(host=config.REDIS_HOST, 
        port=config.REDIS_PORT, 
        max_connections=config.MAX_REDIS_CONNECTION, db=config.REDIS_DB
    )

    return redis.StrictRedis(connection_pool=connection_pool)

