import config as config
from .celery_initialization import task_obj as celery_obj
from twilio.rest import Client

#twilio configs
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

@celery_obj.task
def twilio_send_message(msg_body=None):
	if msg_body:
		try:
			send_to = msg_body.get('receivers',[])
			for item in send_to:
				receiver_no = '+91'+str(item)
				client.messages.create(
					to=receiver_no,
					from_=config.TWILIO_NUMBER,
					body= str(msg_body.get('message'))
				)
		except Exception as e:
			return (False, "message not sent !! error occured.")