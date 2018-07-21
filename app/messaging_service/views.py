from flask import Blueprint, request
from app import app
from handlers.messaging_service import MessageService
from ..helpers import send_response
from jsonschema import validate
from ..decorators import validate_jwt_token

messagingService = Blueprint('messagingService',__name__)

@messagingService.route('/sendMessage', methods = ['POST'])
def send_message():
	message_handler = MessageService(request)
	if request.method == 'POST':
		message_type = request.args.get('type')
		res = message_handler.s_message(message_type)
		return send_response(res)
	return send_response("request method not allowed",405)