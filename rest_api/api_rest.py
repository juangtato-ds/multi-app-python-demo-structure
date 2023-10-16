from pydantic import BaseModel
from typing import Union, List

class TaskReceivedParameters(BaseModel):
    task_name: str
    parameters: List[Union[str, int]]

class TaskResponse(BaseModel):
    task_id: str
    task_response: str

class TaskInfo(BaseModel):
    task_id: str
    task_status: str
    task_result: str