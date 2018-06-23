from flask import Blueprint, request
from app import app
from handlers.user_authentication import UserAuthentication
from ..helpers import send_response
from jsonschema import validate
from ..decorators import validate_jwt_token

user_auth = Blueprint('user_auth',__name__)

@user_auth.route('/register', methods = ['POST'])
def user_register():
	register_handler = UserAuthentication(request)
	if request.method == 'POST':
		res = register_handler.register_user()
		return send_response(res)
	return send_response("request method not allowed",405)

@user_auth.route('/login', methods = ['POST']) 
def user_login():
	login_handler = UserAuthentication(request)
	if request.method == 'POST':
		res = login_handler.login_user()
		return send_response(res)
	return send_response("request method not allowed",405) 

@user_auth.route('/logout/{user_id}', methods = ['GET'])
def user_logout():
	register_hand = UserAuthentication(request)
	return "This is logout"

@user_auth.route('/test', methods = ['GET'])
@validate_jwt_token
def test_api():
	demo_hand = UserAuthentication(request)
	res = demo_hand.demo_method()
	return send_response(res)