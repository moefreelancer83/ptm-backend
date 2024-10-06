from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool
    deadline: Optional[date] = None