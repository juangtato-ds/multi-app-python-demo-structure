from celery_app import app
from celery_app import get_task_info
from api_rest import TaskReceivedParameters
from fastapi import FastAPI
import time

api_app: FastAPI = FastAPI()

@api_app.post("/call_task")
async def call_celery_task(task_parameters: TaskReceivedParameters) -> str:
    result = app.send_task(task_parameters.task_name, task_parameters.parameters)
    time.sleep(2)
    if result.ready():
        return result.get(timeout=5)

@api_app.get("task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    return get_task_info(task_id)

@api_app.get("/health-check")
async def health_check():
    return {'healthcheck': True}
