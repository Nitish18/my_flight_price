from celery import Celery
import config as config


def get_text_celery_task():
	text_task_obj = Celery('text_celery_task',
		broker='redis://'+ str(config.REDIS_HOST) + ':' + str(config.REDIS_PORT) + '/' + '2',
		backend='redis://'+ str(config.REDIS_HOST) + ':' + str(config.REDIS_PORT) + '/' + '3',
		include=['app.messaging_service.celery.text_celery_tasks'])


	return text_task_obj


# def get_audio_celery_task():
# 	audio_task_obj = Celery('audio_celery_task',
# 		broker='redis://'+ str(config.REDIS_HOST).split('://')[1] + ':' + str(config.REDIS_PORT) + '/' + '2',
# 		backend='redis://'+ str(config.REDIS_HOST).split('://')[1] + ':' + str(config.REDIS_PORT) + '/' + '3',
# 		include=['app.messaging_service.celery.audio_celery_task'])
# 	return audio_task_obj