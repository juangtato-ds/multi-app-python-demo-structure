from random import random
from celery import Celery
import time

module_name = 'tasks'
broker_url = 'redis://localhost:6379/0'
# app = Celery(module_name, backend='redis://localhost/1', broker=broker_url)
app = Celery(module_name)
app.config_from_object('celeryconfig')

class MyModel:
    uuid: str
    def __init__(self) -> None:
        self.uuid = str(round(random() * 1000))
    def predict(self, x,y):
        print(f'Requested {self.uuid}: {x} + {y}')
        time.sleep(2)
        return x + y

my_model = MyModel()

@app.task(bind=True,name='sum')
def add(self, x, y):
    print(self.request.id)
    return my_model.predict(x,y)