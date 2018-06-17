from app import app
from app.user_auth.models import Users
from ..models import Users


class UserAuthentication:

	def __init__(self,request):
		self.request = request
		self.user_obj = Users().mongo_connector()

	def register_user(self):
		print self.user_obj.find({})
		return "user is registered"