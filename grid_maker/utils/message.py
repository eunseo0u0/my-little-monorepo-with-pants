import base64
import uuid
from io import BytesIO

import cv2
import numpy as np
from fastapi.responses import StreamingResponse
from PIL import Image
from pydantic import BaseModel, Field


class GridMakerMessage(BaseModel):
    image_files: list[str]
    rows: int
    cols: int
    resize_size: int = Field(256, ge=128, le=512)


def multipart_response(image: np.ndarray | Image.Image) -> StreamingResponse:
    if not isinstance(image, np.ndarray):
        image = np.array(image)

    boundary = f"{uuid.uuid4().hex}"
    content_type = f"multipart/mixed; boundary={boundary}"

    def generate():
        _, img_bytes = cv2.imencode(".png", image)
        img_bytes = img_bytes.tobytes()
        headers = {
            "Content-Disposition": "attachment; filename=grid.png",
            "Content-Type": "image/png",
            "Content-Length": str(len(img_bytes)),
        }
        yield f"--{boundary}\r\n"
        yield b"".join(
            [f"{key}: {value}\r\n".encode("utf-8") for key, value in headers.items()]
        )
        yield b"\r\n"
        yield img_bytes + b"\r\n"
        # End boundary
        yield f"--{boundary}--\r\n"

    headers = {"Content-Type": content_type}

    return StreamingResponse(generate(), headers=headers)


def image_to_base64(input_image: Image.Image) -> str:
    """
    주어진 이미지 객체를 base64 문자열로 인코딩합니다.
    Args:
        input_image (Image.Image): 입력 이미지입니다.
    Returns:
        str: 이미지를 base64로 인코딩한 문자열입니다.
    """

    buffered = BytesIO()
    input_image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_to_image(input_text: str) -> Image.Image:
    """
    base64 인코딩된 문자열을 이미지 객체로 디코딩합니다.
    Args:
        input_text (str): 입력된 base64 문자열입니다.
    Returns:
        Image: 디코딩된 이미지 객체입니다.
    """

    image_data = base64.b64decode(input_text)
    return Image.open(BytesIO(image_data))
