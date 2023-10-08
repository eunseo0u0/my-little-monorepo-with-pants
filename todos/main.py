import argparse

import uvicorn
from fastapi import FastAPI, Request

from todos.apps.monitor import app as app_monitor
from todos.apps.v1.todos import app as app_todos_v1

app = FastAPI(
    title="Grid Maker",
    description="It is a simple API which can create a grid of images.",
)
app.mount("/monitor", app_monitor)
app.mount("/todos/v1", app_todos_v1)


@app.get("/apis")
def apis(request: Request) -> list[str]:
    routes = {route.path for route in request.app.routes}
    routes -= {"/openapi.json", "/docs", "/redoc", "/docs/oauth2-redirect", "/apps"}
    return sorted(list(routes))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grid Maker")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host IP")
    parser.add_argument("--port", type=int, default=8000, help="Port")
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port)
