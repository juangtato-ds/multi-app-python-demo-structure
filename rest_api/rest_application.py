from api_rest import TaskReceivedParameters, TaskResponse, TaskInfo
from fastapi import FastAPI, HTTPException, Body
from celery.result import AsyncResult
from celery import Celery
from typing import Optional
import time

app: FastAPI = FastAPI()

module_name = 'tasks'
celery_app = Celery(module_name)
celery_app.config_from_object('celeryconfig')


@app.post("/call_task")
async def call_celery_task(
    task_parameters: TaskReceivedParameters = Body(
        ...,
        example=TaskReceivedParameters(
            task_name="concatenate", parameters=["pollo", "frito"]
        ),
    )
) -> TaskResponse:
    sended_task = celery_app.send_task(
        task_parameters.task_name, task_parameters.parameters
    )
    time.sleep(2)
    if sended_task.ready():
        result = sended_task.get(timeout=5)
        return TaskResponse(task_id=result["task_id"], task_response=result["result"])
    return TaskResponse(
        task_id=sended_task.id, task_response="IN PROGRESS - Come back soon"
    )


@app.get("/task/{task_id}")
async def get_task_status(task_id: str) -> TaskInfo:
    if task_info := get_task_info(task_id):
        return TaskInfo(
            task_id=task_info["task_result"]["task_id"],
            task_status=task_info["task_status"],
            task_result=task_info["task_result"]["result"],
        )
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.get("/health-check")
async def health_check():
    return {"healthcheck": True}


def get_task_info(task_id) -> Optional[dict]:
    result = None
    task_result = AsyncResult(task_id)
    if task_result.ready():
        result = {"task_status": task_result.status, "task_result": task_result.result}
    return result
