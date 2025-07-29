from PIL import Image
import ascii_magic  # type: ignore

from PIL import Image
import ascii_magic  # type: ignore
import hashlib
import os
import pickle
from typing import Optional

# Cache directory for pre-computed frames
CACHE_DIR = os.path.expanduser("~/.animcli_cache")

def _get_cache_key(gif_path: str, width: float, columns: int) -> str:
    """Generate a unique cache key based on gif path and display parameters."""
    # Include file modification time to invalidate cache if gif changes
    try:
        mtime = os.path.getmtime(gif_path)
        cache_data = f"{gif_path}:{width}:{columns}:{mtime}"
        return hashlib.md5(cache_data.encode()).hexdigest()
    except OSError:
        # Fallback if we can't get mtime
        cache_data = f"{gif_path}:{width}:{columns}"
        return hashlib.md5(cache_data.encode()).hexdigest()

def _load_cached_frames(cache_key: str) -> Optional[list[str]]:
    """Load frames from cache if available."""
    if not os.path.exists(CACHE_DIR):
        return None
    
    cache_file = os.path.join(CACHE_DIR, f"{cache_key}.pkl")
    if not os.path.exists(cache_file):
        return None
    
    try:
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    except (IOError, pickle.PickleError):
        return None

def _save_cached_frames(cache_key: str, frames: list[str]) -> None:
    """Save frames to cache."""
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        cache_file = os.path.join(CACHE_DIR, f"{cache_key}.pkl")
        with open(cache_file, 'wb') as f:
            pickle.dump(frames, f)
    except (IOError, pickle.PickleError):
        pass  # Continue without caching if we can't save

def gif_to_ascii_frames(gif_path: str, width: float, columns: int) -> list[str]:
    """
    Convert GIF frames to ASCII with caching for improved performance.
    """
    # Check cache first
    cache_key = _get_cache_key(gif_path, width, columns)
    cached_frames = _load_cached_frames(cache_key)
    
    if cached_frames is not None:
        return cached_frames
    
    # Generate frames if not in cache
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

    # Cache the generated frames
    _save_cached_frames(cache_key, frames)
    
    return frames

def process_frame(img: Image.Image) -> Image.Image:
    """
    Process frame with optimized transparency handling and color conversion.
    """
    # Fast path for already processed frames
    if img.mode == "RGB":
        return img
    
    # Convert to RGBA for transparency handling
    if img.mode != "RGBA":
        img = img.convert("RGBA")
        
    # Optimize transparency handling for palette mode
    if img.mode == "P" and img.info.get("transparency") is not None:
        img = img.convert("RGBA")
        
        # More efficient transparency replacement using putdata with list comprehension
        data = img.getdata()
        new_data = [(0, 0, 0, 255) if item[3] == 0 else item for item in data]
        img.putdata(new_data)
    
    # Convert to RGB for ASCII conversion (removes alpha channel and improves performance)
    return img.convert("RGB")

def image_to_ascii(img: Image.Image, width: float, columns: int) -> str:
    # Use from_pillow_image for PIL Image objects
    art = ascii_magic.from_pillow_image(img)  # type: ignore
    return art.to_ascii(width_ratio=width, columns=columns)  # type: ignore
