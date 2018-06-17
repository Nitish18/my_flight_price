from flask import Blueprint, request
from app import app
from handlers.user_authentication import UserAuthentication
from ..helpers import send_response
from jsonschema import validate

user_auth = Blueprint('user_auth',__name__)


@user_auth.route('/register', methods = ['POST'])
def user_register():
	register_handler = UserAuthentication(request)
	if request.method == 'POST':
		res = register_handler.register_user()
		return send_response(res[1],res[0])
	return send_response("request method not allowed",405)

@user_auth.route('/login', methods = ['POST'])
def user_login():
	login_handler = UserAuthentication(request)
	if request.method == 'POST':
		res = login_handler.login_user()
		return send_response(res[1],res[0])
	return send_response("request method not allowed",405) 


@user_auth.route('/logout/{user_id}', methods = ['GET'])
def user_logout():
	register_hand = UserAuthentication(request)
	return "This is logout"