import datetime

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from src.todos.models.v1.todos import TodoItem, TodoRetrieve

app = APIRouter()

todo_list: list[TodoItem] = []


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
    try:
        todo_item.id = len(todo_list)
        todo_item.created_at = datetime.datetime.utcnow()
        todo_list.append(todo_item)
        return JSONResponse(
            status_code=200, content={"status": "Add item successfully."}
        )
    except OSError as os_error:
        return JSONResponse(
            status_code=400, content={"error": "OS error: " + str(os_error)}
        )
    except ValueError as val_error:
        return JSONResponse(
            status_code=400, content={"error": "Value error: " + str(val_error)}
        )


@app.put("/update/{todo_id}", tags=["update-todo"], summary="Update TODO item.")
async def update_todo_item(
    todo_id: int,
    todo_item: TodoItem = Body(
        ...,
        examples={
            "title": "An example",
            "description": "This is an example.",
            "completed": False,
        },
    ),
) -> JSONResponse:
    try:
        for todo in todo_list:
            if todo.id == todo_id:
                todo.title = todo_item.title
                todo.description = todo_item.description
                todo.completed = todo_item.completed
                todo.updated_at = datetime.datetime.utcnow()
                todo_list[todo_id] = todo
                return JSONResponse(
                    status_code=200, content={"status": "Update item successfully."}
                )
    except OSError as os_error:
        return JSONResponse(
            status_code=400, content={"error": "OS error: " + str(os_error)}
        )
    except ValueError as val_error:
        return JSONResponse(
            status_code=400, content={"error": "Value error: " + str(val_error)}
        )


@app.get(
    "/retrieve",
    response_model=TodoRetrieve,
    tags=["retrieve-todo"],
    summary="Retrieve TODO items.",
)
async def retrieve_todo_items() -> JSONResponse:
    try:
        return todo_list
    except OSError as os_error:
        return JSONResponse(
            status_code=400, content={"error": "OS error: " + str(os_error)}
        )


@app.delete(
    "/delete/{todo_id}}",
    tags=["delete-todo"],
    summary="Delete TODO item.",
)
async def delete_todo_item(todo_id: int) -> JSONResponse:
    try:
        for todo in todo_list:
            if todo.id == todo_id:
                todo_list.pop(todo_id)
                return JSONResponse(
                    status_code=200, content={"status": "Delete item successfully."}
                )
    except OSError as os_error:
        return JSONResponse(
            status_code=400, content={"error": "OS error: " + str(os_error)}
        )
    except ValueError as val_error:
        return JSONResponse(
            status_code=400, content={"error": "Value error: " + str(val_error)}
        )
