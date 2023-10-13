from celery import Celery
import time
import math
import os

module_name = 'tasks'
app = Celery(module_name)
app.config_from_object('celeryconfig')

def active_wait():
    time.sleep(int(os.environ.get["TASK_ARTIFICIAL_DELAY"]))
    return

@app.task
def concatenate(a: str, b: str, c: str = ""):
    active_wait
    return f"Concatenated string result as: {a} {b} {c}"

@app.task
def exponent(x: int):
    active_wait
    return f"Exponential: {float(math.exp(x))}"

@app.task
def square_root(x: int):
    active_wait
    return f"Square root: {float(math.sqrt(x))}"