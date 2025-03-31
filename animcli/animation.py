import time
import os
import platform

import ascii_magic # type: ignore

def animate(duration: float, cycles: int, frames: list[str]):
    """
    Iterate over the frames, printing and clearing each one to create the animation.
    """
    count = 0

    clear_screen = lambda: os.system('cls' if platform.system() == 'Windows' else 'clear')
    hide_cursor  = lambda: os.system('echo \033[?25l')
    show_cursor  = lambda: os.system('echo \033[?25h')

    hide_cursor()

    try:
        while count < cycles:
            for frame in frames:
                ascii_magic.to_terminal(frame)
                time.sleep(duration)
                
                clear_screen()
                
            count += 1
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
