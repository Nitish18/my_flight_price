import json
from db.mongo_connection import mongo_connection


class Users:

	def __init__(self):
		pass

	def mongo_connector(self):
		return mongo_connection(self)