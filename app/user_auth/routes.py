from flask import Blueprint, request

user_auth = Blueprint('user_auth',__name__)

@user_auth.route('/login')
def user_login():
	return "This is Login Page"