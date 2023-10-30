from datetime import datetime

from fastapi.testclient import TestClient
from freezegun import freeze_time

from src.todos.apps.v1.todos import app


class TestTodosAPI:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.item_id = (
            "46e2f3f1cfb34b7692ca659e71331908"  # randomly generated with uuid4().hex
        )
        cls.todo_db = {
            cls.item_id: {
                "title": "",
                "description": "",
                "completed": False,
                "created_at": "2023-10-31T00:00:00",
                "updated_at": "2023-10-31T00:00:00",
            }
        }

    def test_add_api(self) -> None:
        response = self.client.post(
            url="/add",
            json={"title": "", "description": "", "completed": False},
        )
        assert response.status_code == 200

    def test_update_api(self, mocker) -> None:
        mocker.patch("src.todos.apps.v1.todos.todo_db", self.todo_db)
        response = self.client.put(
            url=f"/update/{self.item_id}",
            json={"title": "", "description": "", "completed": False},
        )
        assert response.status_code == 200
        assert response.json() == {
            "detail": f"Update item: '{self.item_id}' successfully."
        }

    # TODO: fix test
    def test_retrieve_api(self, mocker) -> None:
        mocker.patch("src.todos.apps.v1.todos.todo_db", self.todo_db)
        response = self.client.get(url="/retrieve")
        assert response.status_code == 200
        assert response.json() == {"todo_items": self.todo_db}

    def test_delete_api(self, mocker) -> None:
        mocker.patch("src.todos.apps.v1.todos.todo_db", self.todo_db)
        response = self.client.delete(url=f"/delete/{self.item_id}")
        assert response.status_code == 200
        assert response.json() == {
            "detail": f"Delete item: '{self.item_id}' successfully."
        }
