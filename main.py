import datetime
from typing import List

import uvicorn as uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
import models
from db import Session, engine

app = FastAPI()

database = Session()


class ToDoList(BaseModel):
    id: int
    task: str
    date: datetime.date
    mark_as_done: bool

    class Config:
        orm_mode = True


@app.get('/tasks', response_model=List[ToDoList], status_code=200)
def get_all_tasks():
    return database.query(models.ToDoList).all()


@app.post('/add_task', response_model=ToDoList, status_code=201)
def add_new_task(task: ToDoList):
    new_task = models.ToDoList(
        task=task.task,
        date=task.date,
        done=task.mark_as_done
    )

    database.add(new_task)
    database.commit()

    return new_task


@app.put('/task/{task_id}', response_model=ToDoList, status_code=200)
def make_task_done(task_id: int, task: ToDoList):
    task_to_be_done = database.query(models.ToDoList).filter(models.ToDoList.id == task_id).first()
    task_to_be_done.done = task.mark_as_done

    database.delete(task_to_be_done)
    database.commit()
    return task_to_be_done


if __name__ == "__main__":
    models.Base.metadata.create_all(engine)
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
