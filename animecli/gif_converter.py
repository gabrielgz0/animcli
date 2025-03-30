from PIL import Image
from ascii_magic import from_image # type: ignore

def gif_to_ascii_frames(gif_path: str) -> list[str]:
    img = Image.open(gif_path)
    
    frames: list[str] = []
    try:
        while True:
            ascii_frame = image_to_ascii(img) # convert to ascii
            frames.append(ascii_frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    return frames

def image_to_ascii(img: Image.Image):
    return from_image(img)