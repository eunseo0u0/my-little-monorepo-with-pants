import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(..., title="Description", max_length=100)
    completed: bool = Field(False, title="Completed")


class TodoMetadata(TodoItem):
    id: str = Field(..., title="ID")
    created_at: datetime.datetime = Field(None, title="Created At")
    updated_at: datetime.datetime = Field(None, title="Updated At")


class RetreiveResponse(BaseModel):
    todo_list: list[TodoMetadata] = Field(default=[], title="TODO items")
