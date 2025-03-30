import time
import os
import platform

from .colors import BColors, get_color

def animate(duration: float, cycles: int, frames: list[str], color: str):
    """
    Iterate over the frames, printing and clearing each one to create the animation.
    """
    count = 0
    bcolor = get_color(color)

    # verifica o OS pra adaptar o comando de clear
    clear_screen = lambda: os.system('cls' if platform.system() == 'Windows' else 'clear')

    while count < cycles:
        try:
            for frame in frames:
                print(BColors.colorize(frame, bcolor))
                time.sleep(duration)
                clear_screen()
            count += 1
        except KeyboardInterrupt:
            clear_screen()
            break
