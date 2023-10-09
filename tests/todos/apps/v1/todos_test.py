from fastapi.testclient import TestClient

from src.todos.apps.v1.todos import app


class TestTodosAPI:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.test_todo_item = {
            "id": "0",
            "title": "An example",
            "description": "This is an example.",
            "completed": False,
        }

    def test_add_todo_item_api(self) -> None:
        response = self.client.post(url="/add", json=self.test_todo_item)
        assert response.status_code == 200

    def test_update_todo_item_api(self) -> None:
        response = self.client.put(
            url="/update/{cls.test_todo_item.id}", json=self.test_todo_item
        )
        assert response.status_code == 200

    # def test_retrieve_todo_item_api(self) -> None:
    #     response = self.client.post(url="/retrieve", json={"number1": 1, "number2": 2})

    # def test_delete_todo_item_api(self) -> None:
    #     response = self.client.post(url="/delete", json={"number1": 1, "number2": 2})
