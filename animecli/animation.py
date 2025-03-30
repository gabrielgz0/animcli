import time
import os
import platform

from ascii_magic import to_terminal # type: ignore

def animate(duration: float, cycles: int, frames: list[str]):
    """
    Iterate over the frames, printing and clearing each one to create the animation.
    """
    count = 0

    # verifica o OS pra adaptar o comando de clear
    clear_screen = lambda: os.system('cls' if platform.system() == 'Windows' else 'clear')

    while count < cycles:
        try:
            for frame in frames:
                to_terminal(frame)
                time.sleep(duration)
                clear_screen()
            count += 1
        except KeyboardInterrupt:
            clear_screen()
            break
