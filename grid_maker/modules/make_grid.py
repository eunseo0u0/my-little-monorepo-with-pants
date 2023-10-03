from PIL import Image


def _crop_image(image: Image.Image) -> Image.Image:
    width, height = image.size

    crop_size: int = min(width, height)
    left: int = width // 2 - crop_size // 2
    top: int = height // 2 - crop_size // 2
    right: int = width // 2 + crop_size // 2
    bottom: int = height // 2 + crop_size // 2

    return image.crop((left, top, right, bottom))


def _resize_image(image: Image.Image, resize_size: int) -> Image.Image:
    return image.resize((resize_size, resize_size))


def make_grid(
    image_list: list[Image.Image],
    rows: int,
    cols: int,
    resize_size: int,
) -> Image.Image:
    cropped_image_list: list[Image.Image] = [_crop_image(image) for image in image_list]
    resized_image_list: list[Image.Image] = [
        _resize_image(image, resize_size) for image in cropped_image_list
    ]
    grid: Image.Image = Image.new("RGB", size=(resize_size * cols, resize_size * rows))

    for i, img in enumerate(resized_image_list):
        grid.paste(img, (i % cols, i // cols))
    return grid
