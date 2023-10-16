from celery_app import app
import os

@app.task(name='cron_task')
def cron_task():
    print(f'RUN TASK EVERY {float(os.environ.get("CRON_TASK_DELAY"))} SECONDS')

app.conf.beat_schedule = {
    'run-cron-task': {
        'task': 'cron_task',
        'schedule': float(os.environ.get("CRON_TASK_DELAY"))
    },
}