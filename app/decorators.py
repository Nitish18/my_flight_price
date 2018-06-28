import jwt
import config as config
from functools import wraps
from flask import request
from .helpers import send_response
from db.redis_connection import get_redis_connection


# initialization redis object
redis_obj = get_redis_connection()


def validate_jwt_token(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		user_jwt_token =  request.headers['Authorization']
		algo = []
		algo.append(config.JWT_ALGORITHM)
		user_details =  jwt.decode(str(user_jwt_token), config.JWT_SECRET, algorithms=algo)
		if not session_valid(user_details.get('session_id')):
			return send_response((400,"Session expired ! Either user is logged out or it's session is expired."))
		try:
			jwt.decode(str(user_jwt_token), config.JWT_SECRET, algorithms=algo,verify= True)
		except jwt.ExpiredSignatureError:
			return send_response((400,"Your token expired !!"))
		except jwt.InvalidTokenError:
			return send_response((400,"Token Invalid"))
		except jwt.DecodeError:
			return send_response((400,"Cannot decode your token"))
		return func(*args, **kwargs)
	return decorated_function

def session_valid(session_id):
	if str(session_id) in redis_obj.keys():
		return True
	return False