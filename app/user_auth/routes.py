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

@user_auth.route('/login')
def user_login():
	return "This is login"