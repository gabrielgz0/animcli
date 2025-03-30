import argparse
from animation import animate
from gif_converter import gif_to_ascii_frames

import os
import sys
import pkg_resources

def main():
    parser = argparse.ArgumentParser(
        description="Transform a GIF into ascii and animate it in the terminal"
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
        'gif', 
        type=str, 
        help='GIF path or name (if already default)', 
    )
    
    args = parser.parse_args()

    gif_path = args.gif

    if not os.path.isabs(gif_path):
        gif_path = pkg_resources.resource_filename(
            'animecli', f'gifs/{gif_path}.gif'
        )

    if not os.path.exists(gif_path):
        print(f"{gif_path} not found!")
        sys.exit(1)

    frames = gif_to_ascii_frames(gif_path)

    animate(
        cycles=args.cycles,
        duration=args.duration,
        frames=frames,
        color=args.color
    )

if __name__ == '__main__':
    main()
