import json
from db.mongo_connection import mongo_connection


class Users:

	def mongo_connector(self):
		return mongo_connection(self)