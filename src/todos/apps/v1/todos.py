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

todo_db: dict[str, TodoMetadata] = {}


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
        title=request.title,
        description=request.description,
        completed=request.completed,
        created_at=datetime.datetime.utcnow(),
    )
    item_id: str = uuid4().hex
    todo_db[item_id] = todo_metadata
    return JSONResponse(
        status_code=200,
        content={"detail": f"Add item: '{item_id}' successfully."},
    )


@app.put("/update/{item_id}", tags=["update-todo"], summary="Update TODO item.")
async def update_todo_item(
    item_id: str,
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
        item_id: An ID of todo item to be updated.
        request: Todo item request including title, description and completed.

    Returns:
        JSONResponse with a status code and a detailed message.
    """
    try:
        todo_db[item_id]["title"] = request.title
        todo_db[item_id]["description"] = request.description
        todo_db[item_id]["completed"] = request.completed
        todo_db[item_id]["updated_at"] = datetime.datetime.utcnow()
        return JSONResponse(
            status_code=200,
            content={"detail": f"Update item: '{item_id}' successfully."},
        )
    except KeyError:
        return JSONResponse(
            status_code=404,
            content={"detail": f"Item: '{item_id}' not found."},
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
    return RetreiveResponse(todo_items=todo_db)


@app.delete(
    "/delete/{todo_id}",
    tags=["delete-todo"],
    summary="Delete TODO item.",
)
async def delete_todo_item(item_id: str) -> JSONResponse:
    """Delete todo item.

    Args:
        item_id: An ID of todo item to be deleted.

    Returns:
        JSONResponse with a status code and a detailed message.
    """
    try:
        todo_db.pop(item_id)
        return JSONResponse(
            status_code=200,
            content={"detail": f"Delete item: '{item_id}' successfully."},
        )
    except KeyError:
        return JSONResponse(
            status_code=404,
            content={"detail": f"Item: '{item_id}' not found."},
        )
