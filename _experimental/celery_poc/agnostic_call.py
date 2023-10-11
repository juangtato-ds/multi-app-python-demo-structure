from celery import Celery
from celery.result import AsyncResult

module_name = 'tasks'
app = Celery(module_name)
app.config_from_object('celeryconfig')

result = app.send_task('sum', [4, 5])

print(f'Is {result.id} ready?: {result.ready()}')

task = app.gen_task_name(name='sum', module=module_name)
print(f'Task name: {task}')

import time
time.sleep(5)

res = AsyncResult(result.id, app=app)
print(f'AsyncResult state: {res.state}')
# print(f'AsyncResult state: {res.get(timeout=2)}')



#actual_result = result.get(timeout=5)

#print(f'Actual result: {actual_result}')

print(f'AsyncResult state: {res.state}')
#print(f'AsyncResult state: {res.get()}')
print(res.args)
if res.ready():
  print(res.get(timeout=1))