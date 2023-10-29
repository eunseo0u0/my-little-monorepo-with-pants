import datetime
from uuid import uuid4

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from src.todos.models.v1.todos import (
    RetreiveResponse,
    TodoMetadata,
    TodoRequest,
)

app = FastAPI()

todo_list: list[TodoMetadata] = []


@app.post("/add", tags=["add-todo"], summary="Add TODO item.")
async def add_todo_item(
    request: TodoRequest = Body(
        ...,
        example={
            "title": "An example",
            "description": "This is an example.",
            "completed": False,
        },
    )
) -> JSONResponse:
    """Add todo item.

    Args:
        request: Todo item request including title, description and completed.

    Returns:
        JSONResponse with a status code and a detailed message.
    """
    todo_metadata: TodoMetadata = TodoMetadata(
        id=uuid4().hex,
        title=request.title,
        description=request.description,
        completed=request.completed,
        created_at=datetime.datetime.utcnow(),
    )
    todo_list.append(todo_metadata)
    return JSONResponse(
        status_code=200,
        content={"detail": f"Add item: '{todo_metadata.id}' successfully."},
    )


@app.put("/update/{todo_id}", tags=["update-todo"], summary="Update TODO item.")
async def update_todo_item(
    todo_id: str,
    request: TodoRequest = Body(
        ...,
        example={
            "title": "An example",
            "description": "This is an example.",
            "completed": True,
        },
    ),
) -> JSONResponse:
    """Update todo item.

    Args:
        todo_id: An ID of todo item to be updated.
        request: Todo item request including title, description and completed.

    Returns:
        JSONResponse with a status code and a detailed message.
    """
    for i, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo.title = request.title
            todo.description = request.description
            todo.completed = request.completed
            todo.updated_at = datetime.datetime.utcnow()
            todo_list[i] = todo
            return JSONResponse(
                status_code=200,
                content={"detail": f"Update item: '{todo_id}' successfully."},
            )


@app.get(
    "/retrieve",
    response_model=RetreiveResponse,
    tags=["retrieve-todo"],
    summary="Retrieve TODO items.",
)
async def retrieve_todo_items() -> RetreiveResponse:
    """Retrieve todo items.

    Returns:
        RetreiveResponse with a list of todo items.
    """
    return RetreiveResponse(todo_list=todo_list)


@app.delete(
    "/delete/{todo_id}",
    tags=["delete-todo"],
    summary="Delete TODO item.",
)
async def delete_todo_item(todo_id: str) -> JSONResponse:
    """Delete todo item.

    Args:
        todo_id: An ID of todo item to be deleted.

    Returns:
        JSONResponse with a status code and a detailed message.
    """
    for i, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(i)
            return JSONResponse(
                status_code=200,
                content={"detail": f"Delete item: '{todo_id}' successfully."},
            )
