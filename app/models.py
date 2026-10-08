from pydantic import BaseModel
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(BaseModel):
    id: str
    title: str
    description: str
    repository_url: str
    status: TaskStatus = TaskStatus.PENDING


class TaskResult(BaseModel):
    result_id: str
    task_id: str
    status: TaskStatus
    summary: str
