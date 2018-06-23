import jwt
import config as config
from functools import wraps
from flask import request
from .helpers import send_response

def validate_jwt_token(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		user_jwt_token =  request.headers['Authorization']
		try:
			algo = []
			algo.append(config.JWT_ALGORITHM)
			jwt.decode(str(user_jwt_token), config.JWT_SECRET, algorithms=algo,verify= True)
		except jwt.ExpiredSignatureError:
			return send_response((400,"Your token expired !!"))
		except jwt.InvalidTokenError:
			return send_response((400,"Token Invalid"))
		except jwt.DecodeError:
			return send_response((400,"Cannot decode your token"))
		return func(*args, **kwargs)
	return decorated_function