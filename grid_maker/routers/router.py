from fastapi import APIRouter
from fastapi.responses import JSONResponse
from PIL import Image
from starlette.responses import Response

from grid_maker.modules.make_grid import make_grid
from grid_maker.utils.message import (
    GridMakerMessage,
    base64_to_image,
    multipart_response,
)

router = APIRouter()


@router.post("/grid_maker/v1", tags=["grid_maker"], summary="Grid Maker API")
async def grid_maker_api(message: GridMakerMessage) -> Response:
    try:
        image_list: list[Image.Image] = [
            base64_to_image(image) for image in message.image_files
        ]
        grid: Image.Image = make_grid(
            image_list, message.rows, message.cols, message.resize_size
        )
        return multipart_response(grid)

    except FileNotFoundError as fnf_error:
        return JSONResponse(
            status_code=400, content={"error": "File not found: " + str(fnf_error)}
        )
    except OSError as os_error:
        return JSONResponse(
            status_code=400, content={"error": "OS error: " + str(os_error)}
        )
    except ValueError as val_error:
        return JSONResponse(
            status_code=400, content={"error": "Value error: " + str(val_error)}
        )


@router.get("/monitor/l7check", tags=["health check"], summary="Server health check")
def health_check() -> JSONResponse:
    """서버의 정상작동 여부 확인."""
    return JSONResponse(content={"status": "ok"})
