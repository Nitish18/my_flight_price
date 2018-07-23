from celery import Celery
from kombu import Exchange, Queue
import config as config


task_obj = Celery('celery_tasks',
	broker='redis://'+ str(config.REDIS_HOST) + ':' + str(config.REDIS_PORT) + '/' + '2',
	backend='redis://'+ str(config.REDIS_HOST) + ':' + str(config.REDIS_PORT) + '/' + '3',
	include=['app.messaging_service.celery.all_celery_tasks'])


task_obj.conf.task_queues = (
    Queue('low', Exchange('low'), routing_key='low'),
    Queue('medium',  Exchange('medium'), routing_key='medium'),
    Queue('high',  Exchange('high'), routing_key='high'),
)
