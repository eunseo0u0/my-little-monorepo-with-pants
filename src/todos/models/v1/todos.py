import datetime

from pydantic import BaseModel, Field


class TodoMetadata(BaseModel):
    """Todo metadata."""

    id: str = Field(..., title="ID")
    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(..., title="Description", max_length=100)
    completed: bool = Field(default=False, title="Completed")
    created_at: datetime.datetime = Field(..., title="Created At")
    updated_at: datetime.datetime = Field(default=None, title="Updated At")


class TodoRequest(BaseModel):
    """Todo request model used in /add and /update."""

    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(..., title="Description", max_length=100)
    completed: bool = Field(default=False, title="Completed")


class RetreiveResponse(BaseModel):
    """Retrieve response model used in /retrieve."""

    todo_list: list[TodoMetadata] = Field(default=[], title="TODO items")
