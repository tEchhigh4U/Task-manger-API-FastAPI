from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="task-manager",
            user="root",
            password="root"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Create a connection to the database
connection = create_connection()

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

# get all tasks
@app.get("/tasks")
def get_all_tasks():
    return {"tasks": tasks}

# create a task
@app.post("/tasks")
def create_task(task: Task):
    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert a new task
        insert_query = 
        "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)"
        task_data = (task.title, task.description, task.status)
        cursor.execute(insert_query, task_data)

        # Commit the changes to the database
        connection.commit()

        # Return the task
        task_id = cursor.lastrowid

        # Close the cursor and connection to the database
        cursor.close()

        # Return the task
        result = {
            "id": task_id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        }
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return {"Error": "Failed to create task"}

# get a task by id
@app.get("/tasks/{task_id}")
def get_task(task_id: int, task: Task):
    if task_id == task.id:
        result = {"task_id": task_id, 
                  "title": Task.title, 
                    "description": Task.description, 
                    "status": Task.status}
        return result
    return {"message": "Task not found"}

# delete a task by id
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t["id"] == task.id:
            t.update(task.dict())
        return t
    return {"message": "Task not found"}



