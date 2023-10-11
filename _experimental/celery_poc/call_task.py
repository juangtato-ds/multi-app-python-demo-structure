import time
from tasks import add

result = add.delay(4, 4)


time.sleep(5)
print(f'Is {result.id} ready?: {result.ready()}')


actual_result = None
if result.ready():
  actual_result = result.get(timeout=1)

print(f'Actual result: {actual_result}')