import jwt
import config as config


def validate_jwt_token(func):
	def wraps(request):
		try:
			jwt_algo = list(config.JWT_ALGORITHM)
	    	jwt.decode(jwt_token, config.JWT_SECRET, algorithms = jwt_algo)
	    	return func
		except jwt.ExpiredSignatureError:
		    raise e
		except jwt.InvalidTokenError:
			raise e
		except jwt.DecodeError:
			raise e
	return wraps