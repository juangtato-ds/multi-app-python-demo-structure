from celery import Celery
from celery.result import AsyncResult
from typing import Optional

module_name = 'tasks'
app = Celery(module_name)
app.config_from_object('celeryconfig')

def get_task_info(task_id) -> Optional[dict]:
    result = None
    task_result = AsyncResult(task_id)
    if task_result.ready():
        result = {
            "task_status": task_result.status,
            "task_result": task_result.result
        }
    return result