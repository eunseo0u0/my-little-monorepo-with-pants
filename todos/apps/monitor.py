from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/l7check", tags=["health check"], summary="Server health check")
def health_check() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})
