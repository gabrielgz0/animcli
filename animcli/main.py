import argparse
import os
import sys
import importlib.resources

from .animation import animate
from .gif_converter import gif_to_ascii_frames

GIFS_DIR = importlib.resources.files('animcli') / 'gifs'

def list_gifs():
    for file in GIFS_DIR.iterdir():
        print(str(file.name)[:-4])

def main():
    parser = argparse.ArgumentParser(
        description="Transform a GIF into ASCII and animate it in the terminal"
    )

    parser.add_argument(
        '--cycles', 
        type=int, 
        help='The number of cycles the animation runs.',
        default=100
    )
    
    parser.add_argument(
        '--duration', 
        type=float, 
        help='The length of time between each frame.', 
        default=0.05
    )

    parser.add_argument(
        '--width', 
        type=float, 
        help='The width-ratio that the gif will be displayed', 
        default=2.2
    )

    parser.add_argument(
        '--columns', 
        type=int, 
        help='The size in columns where the gif will be displayed', 
        default=60
    )

    parser.add_argument(
        '--list', 
        action='store_true',
        help='List default gifs.',
    )

    parser.add_argument(
        '--gif', 
        type=str, 
        help='GIF path or name (if already default)', 
    )
    
    args = parser.parse_args()

    if args.list:
        list_gifs()
        sys.exit(0)

    if not args.gif:
        print("No gif specified")
        sys.exit(1)

    gif_path = args.gif
    if not os.path.isabs(gif_path):
        gif_path = str(GIFS_DIR / f"{gif_path}.gif")

    if not os.path.exists(gif_path):
        print(f"Error: '{gif_path}' not found!")
        sys.exit(1)

    frames = gif_to_ascii_frames(gif_path, args.width, args.columns)

    animate(
        cycles=args.cycles,
        duration=args.duration,
        frames=frames,
    )

if __name__ == '__main__':
    main()
