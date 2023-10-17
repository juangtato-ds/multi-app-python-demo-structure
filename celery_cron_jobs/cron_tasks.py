from random import random
from celery import Celery
import os

module_name = 'tasks'
app = Celery(module_name)
app.config_from_object('celeryconfig')

@app.task(name='cron_task')
def cron_task():
    print(f'RUN TASK EVERY {float(os.environ.get("CRON_TASK_DELAY", "120"))} SECONDS')
    return random()

app.conf.beat_schedule = {
    'run-cron-task': {
        'task': 'cron_task',
        'schedule': float(os.environ.get("CRON_TASK_DELAY", '120'))
    },
    'run-other-task-in-other-machine': {
        'task': 'concatenate',
        'schedule': float(os.environ.get("CRON_TASK_DELAY", '120')),
        'args': ('pollo', 'frito')
    }
}
