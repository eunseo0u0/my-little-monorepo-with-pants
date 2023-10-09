import datetime

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from src.todos.models.v1.todos import RetreiveResponse, TodoItem

app = FastAPI()

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
    todo_item.id = len(todo_list)
    todo_item.created_at = datetime.datetime.utcnow()
    todo_list.append(todo_item)
    return JSONResponse(status_code=200, content={"status": "Add item successfully."})


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
    tags=["retrieve-todo"],
    summary="Retrieve TODO items.",
)
async def retrieve_todo_items() -> dict:
    return {"todo_items": todo_list}


@app.delete(
    "/delete/{todo_id}",
    tags=["delete-todo"],
    summary="Delete TODO item.",
)
async def delete_todo_item(todo_id: int) -> JSONResponse:
    for i, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(i)
            return JSONResponse(
                status_code=200, content={"status": "Delete item successfully."}
            )
