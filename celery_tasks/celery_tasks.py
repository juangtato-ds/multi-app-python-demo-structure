from celery_app import app
import time
import math
import os

def active_wait():
    time.sleep(int(os.environ.get("TASK_ARTIFICIAL_DELAY")))
    return

@app.task(bind=True, name='concatenate')
def concatenate(self, a: str, b: str, c: str = "") -> str:
    active_wait
    return {
        "task_id": self.request.id, 
        "result": f"Concatenated string result as: {a} {b} {c}"
        }

@app.task(bind=True, name='exponential')
def exponent(self, x: int) -> str:
    active_wait
    return {
        "task_id": self.request.id, 
        "result": f"Exponential: {float(math.exp(x))}"
    }

@app.task(bind=True, name='sqrt')
def square_root(self, x: int) -> str:
    active_wait
    return {
        "task_id": self.request.id, 
        "result": f"Square root: {float(math.sqrt(x))}"
    }
