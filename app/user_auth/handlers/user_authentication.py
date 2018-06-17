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


	def login_user(self):

		user_creds = self.request.json
		if self.user_already_exists(str(user_creds['email'])):
			valid_user_creds = self.check_user_creds(user_creds)
			if valid_user_creds:
				return (200,"user successfully loged in !!")
			return (401, "wrong login details")
		return (400, "user does not exist !!")

	def check_user_creds(self, user_creds):
		user_pass = self.user_obj.find_one({'email': user_creds['email']},{'pass': 1})
		if str(user_pass['pass']) == str(user_creds['pass']):
			return True
		return False	