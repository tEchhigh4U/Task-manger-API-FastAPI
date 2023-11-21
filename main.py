from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

# Sample data - replace with your own data storage mechanism
tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "status": "todo"},
    {"id": 2, "title": "Task 2", "description": "Description 2", "status": "in progress"},
    {"id": 3, "title": "Task 3", "description": "Description 3", "status": "done"},
]

# get all tasks
@app.get("/tasks")
def get_all_tasks():
    return {"tasks": tasks}

# create a task
@app.post("/tasks")
def create_task(task: Task):
    result = {"title": Task.title, "description": Task.description, "status": Task.status}
    return result

# get a task by id
@app.get("/tasks/{task_id}")
def get_task(task_id: int, task: Task):
    if task_id == task.id:
        result = {"task_id": task_id, "title": Task.title, 
                    "description": Task.description, "status": Task.status}
        return result
    return result

# delete a task by id
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t["id"] == task.id:
            t.update(task.dict())
        return t
    return {"message": "Task not found"}



