import argparse

import uvicorn
from fastapi import FastAPI

from grid_maker.routers.router import router

app = FastAPI(
    title="Grid Maker",
    description="It is a simple API which can create a grid of images.",
)
app.include_router(router)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grid Maker")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host IP")
    parser.add_argument("--port", type=int, default=8000, help="Port")
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port)
