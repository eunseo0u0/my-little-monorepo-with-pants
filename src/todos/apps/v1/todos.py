import datetime
from uuid import uuid4

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from src.todos.models.v1.todos import (
    RetreiveResponse,
    TodoItem,
    TodoMetadata,
)

app = FastAPI()

todo_list: list[TodoMetadata] = []


@app.post("/add", tags=["add-todo"], summary="Add TODO item.")
async def add_todo_item(
    todo_item: TodoItem = Body(
        ...,
        examples={
            "title": "An example",
            "description": "This is an example.",
            "completed": False,
        },
    )
) -> JSONResponse:
    todo_metadata: TodoMetadata = TodoMetadata(
        id=uuid4().hex,
        title=todo_item.title,
        description=todo_item.description,
        completed=todo_item.completed,
        created_at=datetime.datetime.utcnow(),
    )
    todo_list.append(todo_metadata)
    return JSONResponse(status_code=200, content={"status": "Add item successfully."})


@app.put("/update/{todo_id}", tags=["update-todo"], summary="Update TODO item.")
async def update_todo_item(
    todo_id: str,
    todo_item: TodoItem = Body(
        ...,
        examples={
            "title": "An example",
            "description": "This is an example.",
            "completed": False,
        },
    ),
) -> JSONResponse:
    for i, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo.title = todo_item.title
            todo.description = todo_item.description
            todo.completed = todo_item.completed
            todo.updated_at = datetime.datetime.utcnow()
            todo_list[i] = todo
            return JSONResponse(
                status_code=200, content={"status": "Update item successfully."}
            )


@app.get(
    "/retrieve",
    response_model=RetreiveResponse,
    tags=["retrieve-todo"],
    summary="Retrieve TODO items.",
)
async def retrieve_todo_items() -> RetreiveResponse:
    return RetreiveResponse(todo_list=todo_list)


@app.delete(
    "/delete/{todo_id}",
    tags=["delete-todo"],
    summary="Delete TODO item.",
)
async def delete_todo_item(todo_id: str) -> JSONResponse:
    for i, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(i)
            return JSONResponse(
                status_code=200, content={"status": "Delete item successfully."}
            )
