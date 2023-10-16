from celery_app import app
from celery_tasks import concatenate
import os

# @app.on_after_configure.connect
# def setup_cron_tasks(sender, **kwargs):
#     sender.add_periodic_task(int(os.environ.get("CRON_TASK_DELAY")), 
#                              concatenate.s("Hello", "World"), 
#                              name='run_cron_task')

app.conf.beat_schedule = {
    'run_cron_task': {
        'task': 'tasks.exponent',
        'schedule': int(os.environ.get("CRON_TASK_DELAY")),
        'args': (2)
    }
}