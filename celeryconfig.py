import os

broker_transport = os.environ.get("CELERY_BROKER_TRANSPORT")
backend_transport = os.environ.get("CELERY_BACKEND_TRANSPORT")
broker_host = os.environ.get("CELERY_HOST_BROKER")
backend_host = os.environ.get("CELERY_HOST_BACKEND")
broker_port = os.environ.get("CELERY_BROKER_PORT")
backend_port = os.environ.get("CELERY_BACKEND_PORT")
# virtual_host = os.environ.get("CELERY_VIRTUAL_HOST"))
db = os.environ.get("CELERY_DB")

# Broker settings
# broker_url = 'transport://userid:password@hostname:port/virtual_host'
broker_url = f'{broker_transport}://{broker_host}:{broker_port}'

# Backend settings
# result_backend = 'redis://username:password@host:port/db'
result_backend = f'{backend_transport}://{backend_host}:{backend_port}'

timezone = 'Europe/Madrid'

imports = ('celery_tasks.celery_tasks')
