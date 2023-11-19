from fastapi.testclient import TestClient

from src.todos.apps.v1.todos import app
from src.todos.models.v1.todos import TodoMetadata


class TestTodosAPI:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.item_id = (
            "46e2f3f1cfb34b7692ca659e71331908"  # randomly generated with uuid4().hex
        )
        cls.todo_item = TodoMetadata(
            title="",
            description="",
            completed=False,
            created_at="2023-10-31T00:00:00",
            updated_at="2023-11-01T00:00:00",
        )

    def test_add_api_req_succeeded(self) -> None:
        """Test `add` API with a valid request."""
        response = self.client.post(
            url="/add",
            json={"title": "", "description": "", "completed": False},
        )
        assert response.status_code == 200

    def test_add_api_req_failed_wrong_entity(self) -> None:
        """Test `add` API with a wrong entity."""
        response = self.client.post(
            url="/add",
            json={"description": "", "completed": False},
        )
        assert response.status_code == 422  # Unprocessable Entity

    def test_update_api_req_succeeeded(self, mocker) -> None:
        """Test `update` API with a valid request."""
        mocker.patch("src.todos.apps.v1.todos.todo_db", {self.item_id: self.todo_item})
        datetime_mock = mocker.patch("src.todos.apps.v1.todos.datetime.datetime")
        datetime_mock.utcnow.return_value = "2023-11-01T00:00:00"

        response = self.client.put(
            url=f"/update/{self.item_id}",
            json={"title": "", "description": "", "completed": False},
        )
        assert response.status_code == 200
        assert response.json() == {
            "detail": f"Update item: '{self.item_id}' successfully."
        }

    def test_update_api_req_failed_wrong_entity(self, mocker) -> None:
        """Test `update` API with a wrong entity."""
        mocker.patch("src.todos.apps.v1.todos.todo_db", {self.item_id: self.todo_item})

        response = self.client.put(
            url=f"/update/{self.item_id}",
            json={"description": "", "completed": False},
        )
        assert response.status_code == 422  # Unprocessable Entity

    def test_update_api_req_failed_nonexistent_id(self, mocker) -> None:
        """Test `update` API with a non-existent todo item."""
        mocker.patch(
            "src.todos.apps.v1.todos.todo_db",
            {self.item_id: self.todo_item},
        )

        response = self.client.put(
            url="/update/-1",
            json={"title": "", "description": "", "completed": False},
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "Item: '-1' is not found."}

    def test_retrieve_api(self, mocker) -> None:
        """Test `retrieve` API."""
        mocker.patch("src.todos.apps.v1.todos.todo_db", {self.item_id: self.todo_item})

        response = self.client.get(url="/retrieve")
        assert response.status_code == 200
        assert response.json() == {
            "todo_items": {self.item_id: self.todo_item.model_dump(mode="json")}
        }

    def test_delete_api_succeeded(self, mocker) -> None:
        """Test `delete` API with a valid request."""
        mocker.patch("src.todos.apps.v1.todos.todo_db", {self.item_id: self.todo_item})

        response = self.client.delete(url=f"/delete/{self.item_id}")
        assert response.status_code == 200
        assert response.json() == {
            "detail": f"Delete item: '{self.item_id}' successfully."
        }

    def test_delete_api_failed_nonexistent_id(self, mocker) -> None:
        """Test `delete` API with a non-existent todo item."""
        mocker.patch("src.todos.apps.v1.todos.todo_db", {self.item_id: self.todo_item})

        response = self.client.delete(
            url="/delete/-1",
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "Item: '-1' is not found."}
