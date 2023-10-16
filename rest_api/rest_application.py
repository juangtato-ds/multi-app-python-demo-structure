from celery_app import app
from celery_app import get_task_info
from rest_api.api_rest import TaskReceivedParameters, TaskResponse, TaskInfo
from fastapi import FastAPI, HTTPException
import time

api_app: FastAPI = FastAPI()


@api_app.post("/call_task")
async def call_celery_task(task_parameters: TaskReceivedParameters) -> TaskResponse:
    sended_task = app.send_task(task_parameters.task_name, task_parameters.parameters)
    time.sleep(2)
    if sended_task.ready():
        result = sended_task.get(timeout=5)
        return TaskResponse(task_id=result["task_id"], task_response=result["result"])
    return TaskResponse(
        task_id=sended_task.id, task_response="IN PROGRESS - come back soon"
    )


@api_app.get("/task/{task_id}")
async def get_task_status(task_id: str) -> TaskInfo:
    task_info = get_task_info(task_id)
    if task_info:
        return TaskInfo(
            task_id=task_info["task_result"]["task_id"],
            task_status=task_info["task_status"],
            task_result=task_info["task_result"]["result"],
        )
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@api_app.get("/health-check")
async def health_check():
    return {"healthcheck": True}
