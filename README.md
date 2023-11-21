# Task-Manager-API
Create a simple Task Manager API using FastAPI. The API will allow users to manage their tasks by performing CRUD operations on a task resource.

## Requirements:

1. Users should be able to create a new task by sending a POST request to the /tasks endpoint. Each task should have a title, description, and status (e.g., "todo", "in progress", "done").
2. Users should be able to retrieve a list of all tasks by sending a GET request to the /tasks endpoint.
3. Users should be able to retrieve a specific task by its ID by sending a GET request to the /tasks/{task_id} endpoint.
4. Users should be able to update a task by sending a PUT request to the /tasks/{task_id} endpoint, providing the updated task data.
5. Users should be able to delete a task by sending a DELETE request to the /tasks/{task_id} endpoint.
6. Implement input validation to ensure that the required fields are provided when creating or updating a task.
7. Add error handling and appropriate responses for invalid requests or non-existent resources.
