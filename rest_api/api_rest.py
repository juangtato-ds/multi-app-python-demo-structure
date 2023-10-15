from pydantic import BaseModel
from typing import Union, List

class TaskReceivedParameters(BaseModel):
    task_name: str
    parameters: List[Union[str, int]]