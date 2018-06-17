from app import app
from app.user_auth.models import Users
from ..models import Users
from jsonschema import validate
from ...helpers import current_epoch


class UserAuthentication:

	def __init__(self,request):
		self.request = request
		self.user_obj = Users().mongo_connector()

	def register_user(self):
		valid_user_info = Users().sample_json_schema()
		valid_json_schema = valid_user_info[0]
		req_keys = valid_user_info[1]

		user_info = self.request.json

		try:
			validate(user_info,valid_json_schema)
			if self.user_already_exists(str(user_info['email'])):
				return (400, "user already exists")
			
			user_info['is_active'] = True
			user_info['created'] = current_epoch()
			self.user_obj.insert_one(user_info)
			
			return (200, "User registered !!!")
		
		except Exception as e:
			return (400,"please check input !!")


	def user_already_exists(self,user_email):
		if self.user_obj.find_one({'email':user_email,'is_active':True}):
			return True
		return False