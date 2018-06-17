from flask import Blueprint, request
from app import app
from handlers.user_registration import UserRegistration

user_auth = Blueprint('user_auth',__name__)

@user_auth.route('/register', methods = ['POST'])
def user_register():
	if request.method == 'POST':
		register_hand = UserRegistration()
		return register_hand.register_user()
	return "This is registration"


@user_auth.route('/login', methods = ['POST'])
def user_login():
	register_hand = UserRegistration()
	return "This is login"


@user_auth.route('/logout/{user_id}', methods = ['GET'])
def user_logout():
	register_hand = UserRegistration()
	return "This is logout"