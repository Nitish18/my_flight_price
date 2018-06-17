import json
from db.mongo_connection import mongo_connection
from passlib.hash import pbkdf2_sha256 as sha256


class Users:

	def __init__(self):
		pass

	def mongo_connector(self):
		return mongo_connection(self)

	def sample_json_schema(self):
		json_schema = {
			"type" : "object",
		     "properties" : {
		     	"name" : {"type" : "string"},
		        "email" : {"type" : "string"},
		        "pass" : {"type" : "string"},
		     },
 		}
 		required_keys = ['email','pass','name']
		return (json_schema,required_keys)

	@staticmethod
	def generate_hash(password):
		return sha256.hash(password)

	@staticmethod
	def verify_hash(password, hash):
		return sha256.verify(password, hash)