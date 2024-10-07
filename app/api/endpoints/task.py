from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models.task import Task, TaskResponse, TaskCreate
from app.db.database import get_session
from app.services.task_service import TaskService
from typing import List, Optional

router = APIRouter()


@router.post('/', response_model=TaskResponse)
async def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    task_service = TaskService(session=session)
    return task_service.create_task(task)

#TODO error handling
@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: str, session: Session = Depends(get_session)):
    task_service = TaskService(session=session)
    deleted_task = task_service.delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task

@router.get('/', response_model=List[TaskResponse])
async def get_all_tasks(session: Session = Depends(get_session)):
    task_service = TaskService(session=session)
    return task_service.get_all_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str, session: Session= Depends(get_session)):
    task_service = TaskService(session=session)
    task = task_service.get_task(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
    
@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: str, task_data: Task, session: Session = Depends(get_session)):
    task_service = TaskService(session=session)
    updated_task = task_service.update_task(task_id=task_id, task=task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task