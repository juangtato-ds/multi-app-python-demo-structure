from random import random
from celery import Celery
import time
import math
import os

module_name = 'tasks'
app = Celery(module_name)
app.config_from_object(str(os.environ.get("CELERY_CONF_PATH", "celeryconfig")))

def active_wait():
    time.sleep(int(os.environ.get("TASK_ARTIFICIAL_DELAY", '5')))
    return

@app.task(bind=True, name='concatenate')
def concatenate(self, a: str, b: str, c: str = "") -> dict:
    active_wait()
    return {
        "task_id": self.request.id,
        "result": f"Concatenated string result as: {a} {b} {c}"
        }

@app.task(bind=True, name='exponential')
def exponent(self, x: int) -> dict:
    active_wait()
    return {
        "task_id": self.request.id,
        "result": f"Exponential: {float(math.exp(x))}"
    }

@app.task(bind=True, name='sqrt')
def square_root(self, x: int) -> dict:
    active_wait()
    return {
        "task_id": self.request.id,
        "result": f"Square root: {float(math.sqrt(x))}"
    }

@app.task(bind=True, name='cron_task')
def cron_task(self) -> float:
    active_wait()
    print('Executing cront_task')
    return random()