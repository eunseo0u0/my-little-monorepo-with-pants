from fastapi.testclient import TestClient

from src.todos.apps.monitor import app


class TestMonitorAPI:
    client = TestClient(app)

    def test_health_check_api(self) -> None:
        """Test server health check."""
        response = self.client.get(url="/l7check")
        assert response.status_code == 200
