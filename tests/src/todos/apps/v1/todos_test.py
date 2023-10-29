from fastapi.testclient import TestClient

from src.todos.apps.v1.todos import app
from src.todos.models.v1.todos import (
    RetreiveResponse,
    TodoMetadata,
    TodoRequest,
)


class TestTodosAPI:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)

    def test_add_api(self) -> None:
        response = self.client.post(
            url="/add",
            json={"title": "test", "description": "test", "completed": False},
        )
        assert response.status_code == 200

    def test_update_api_success(self, mocker) -> None:
        mocker.patch(
            "src.todos.apps.v1.todos.todo_db",
            {
                "0": {
                    "title": "",
                    "description": "",
                    "completed": False,
                    "created_at": "2021-10-10T00:00:00.000000",
                    "updated_at": None,
                }
            },
        )
        response = self.client.put(
            url="/update/0",
            json={"title": "", "description": "", "completed": True},
        )
        assert response.status_code == 200
        assert response.content == {"detail": "Update item: '0' successfully."}

    def test_retrieve_api(self, mocker) -> None:
        mocker.patch(
            "src.todos.apps.v1.todos.todo_db",
            {
                "0": {
                    "title": "",
                    "description": "",
                    "completed": False,
                    "created_at": "2021-10-10T00:00:00",
                    "updated_at": "2021-10-10T00:00:00",
                }
            },
        )
        response = self.client.get(url="/retrieve")
        assert response.status_code == 200
        assert response.json() == {
            "todo_items": {
                "0": {
                    "title": "",
                    "description": "",
                    "completed": False,
                    "created_at": "2021-10-10T00:00:00",
                    "updated_at": "2021-10-10T00:00:00",
                }
            }
        }

    def test_delete_api(self, mocker) -> None:
        mocker.patch(
            "src.todos.apps.v1.todos.todo_db",
            {
                "0": {
                    "title": "",
                    "description": "",
                    "completed": False,
                    "created_at": "2021-10-10T00:00:00",
                    "updated_at": "2021-10-10T00:00:00",
                }
            },
        )
        response = self.client.delete(url="/delete/0")

        assert response.status_code == 200
        assert response.content == {"detail": "Delete item: '0' successfully."}
