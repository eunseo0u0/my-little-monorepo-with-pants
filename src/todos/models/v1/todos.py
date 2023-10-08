import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: int = Field(default=-1, title="ID")
    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(..., title="Description", max_length=100)
    completed: bool = Field(False, title="Completed")
    created_at: datetime.datetime = Field(None, title="Created At")
    updated_at: datetime.datetime = Field(None, title="Updated At")


class TodoRetrieve(TodoItem):
    todo_items: list[TodoItem]
