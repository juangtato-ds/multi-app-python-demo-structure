import os

broker_transport = os.environ.get("CELERY_BROKER_TRANSPORT")
broker_host = os.environ.get("CELERY_HOST_BROKER")
broker_port = os.environ.get("CELERY_BROKER_PORT")
# virtual_host = os.environ.get("CELERY_VIRTUAL_HOST"))

broker_url = f'{broker_transport}://{broker_host}:{broker_port}'
