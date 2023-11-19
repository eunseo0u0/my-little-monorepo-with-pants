from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/l7check", tags=["health check"], summary="Server health check")
def health_check() -> JSONResponse:
    """Check server health.

    Returns:
        JSONResponse with status message
    """
    return JSONResponse(content={"status": "ok"})
