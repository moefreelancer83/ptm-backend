from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = Field(default=False)
    deadline: Optional[date] = None

class TaskCreate(SQLModel):
    title: str
    description: str

class TaskResponse(Task):
    pass