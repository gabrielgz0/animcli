from PIL import Image

def gif_to_ascii_frames(gif_path: str) -> list[str]:
    img = Image.open(gif_path)
    
    frames: list[str] = []
    try:
        while True:
            img_gray = img.convert("L") # grayscale
            width = 100
            height = int(width * 0.5)  # 2:1 (width x height)
            img_gray = img_gray.resize(size=(width, height)) # type: ignore
            ascii_frame = image_to_ascii(img_gray) # convert to ascii
            frames.append(ascii_frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    return frames

def image_to_ascii(img: Image.Image):
    ascii_chars = '@%#*+=-. '
    pixels = img.getdata() # type: ignore
    ascii_str = ''.join([ascii_chars[pixel // 32] if pixel > 50 else ' ' for pixel in pixels])  # type: ignore # space for light pixels
    ascii_str = '\n'.join([ascii_str[i:i+100] for i in range(0, len(ascii_str), 100)])
    return ascii_str