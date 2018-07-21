import config as config
import json
import uuid
from app import app
from ..models import MessageRequest
from jsonschema import validate
from ...helpers import current_epoch
from datetime import timedelta
from ...decorators import validate_jwt_token
from db.redis_connection import get_redis_connection


class MessageService:

	def __init__(self,request):
		self.request = request
		self.redis_obj = get_redis_connection()
		self.message_request = MessageRequest()
		self.message_request_obj = self.message_request.mongo_connector()


		
	
	def s_message(self,message_type):
		msg_payload =  self.request.json
		if message_type in ['text']:
			
			self.save_message_logs(msg_payload)



		return "hello"

	
	def save_message_logs(self, msg_log = None):
		if msg_log:
			# inserting message log into mongo.
			msg_req_log = {
				'id' : str(uuid.uuid4()),
				'message': msg_log.get('message'),
				'receivers': msg_log.get('receivers'),
				'isDeleivered': False
			}
			self.message_request_obj.insert(msg_req_log)