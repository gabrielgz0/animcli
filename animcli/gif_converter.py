from PIL import Image
import ascii_magic  # type: ignore

def gif_to_ascii_frames(gif_path: str, width: float, columns: int) -> list[str]:
    img = Image.open(gif_path)
    
    frames: list[str] = []
    try:
        while True:
            # Convert frame to an image with transparency handled correctly
            frame = process_frame(img)
            
            ascii_frame = image_to_ascii(frame, width, columns)  # Convert to ASCII
            frames.append(ascii_frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    return frames

def process_frame(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    
    if img.mode == "P" and img.info.get("transparency") is not None:
        img = img.convert("RGBA")
        
        data = img.getdata() # type: ignore
        new_data = []
        
        for item in data: # type: ignore
            if item[3] == 0:
                new_data.append((0, 0, 0, 255))  # type: ignore
            else:
                new_data.append(item)  # type: ignore
        
        img.putdata(new_data) # type: ignore
    
    return img

def image_to_ascii(img: Image.Image, width: float, columns: int) -> str:
    return ascii_magic.from_image(img=img, width_ratio=width, columns=columns)  # type: ignore
