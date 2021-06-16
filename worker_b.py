from celery import Celery

# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'

# Initialize celery
_celery = Celery('worker_b', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@_celery.task
def sub_nums(a, b):
    return a - b