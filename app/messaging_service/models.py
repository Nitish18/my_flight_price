import json
from db.mongo_connection import mongo_connection
from passlib.hash import pbkdf2_sha256 as sha256


class MessageRequest:

	def __init__(self):
		pass

	def mongo_connector(self):
		return mongo_connection(self)