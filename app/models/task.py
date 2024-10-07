from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class TaskBase(SQLModel):
    title: str
    description: str
    deadline: Optional[date] = None
    completed: bool = Field(default=False)

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
class TaskCreate(TaskBase):
    pass

class TaskResponse(Task):
    id: int
