from typing import List, Optional
from sqlmodel import Session, select
from app.models.task import Task, TaskCreate, TaskResponse

class TaskService:

    def __init__(self, session: Session) -> None:
        self.session = session

    def create_task(self, task: TaskCreate) -> TaskResponse:
        db_task = Task.model_validate(task)
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskResponse.model_validate(db_task)
    
    def delete_task(self, task_id: str) -> Optional[TaskResponse]:
        db_task = self.session.get(Task, task_id)
        if db_task:
            self.session.delete(db_task)
            self.session.commit()
            return TaskResponse.model_validate(db_task)
        return None
    
    def get_all_tasks(self)-> List[TaskResponse]:
        query = select(Task)
        db_tasks = self.session.exec(query).all()
        return [TaskResponse.model_validate(task) for task in db_tasks]
    
    def get_task(self, task_id: str) -> Optional[TaskResponse]:
        db_task = self.session.get(Task, task_id)
        if db_task:
            return TaskResponse.model_validate(db_task)
        return None
    
    def update_task(self, task_id: str, task: TaskCreate) -> Optional[TaskResponse]:
        db_task_to_update = self.session.get(Task, task_id)
        if db_task_to_update:
            task_data = task.model_dump(exclude_unset=True)
            db_task_to_update.sqlmodel_update(task_data)
            self.session.add(db_task_to_update)
            self.session.commit()
            self.session.refresh(db_task_to_update)
            return TaskResponse.model_validate(db_task_to_update)
        return None





