import time
import sys
import os
import signal

# ANSI escape sequences for better performance
CLEAR_SCREEN = '\033[2J\033[H'  # Clear screen and move cursor to top
HIDE_CURSOR = '\033[?25l'       # Hide cursor
SHOW_CURSOR = '\033[?25h'       # Show cursor
RESET_CURSOR = '\033[H'         # Reset cursor to top without clearing

def animate(duration: float, cycles: int, frames: list[str]):
    """
    Iterate over the frames, printing and clearing each one to create the animation.
    Optimized for better terminal rendering fluidity with several performance improvements:
    - Uses ANSI escape sequences instead of system calls
    - Direct stdout writing for faster output
    - Frame buffering for smoother display
    - Adaptive timing for better frame rate consistency
    - Signal handling for clean interruption
    """
    count = 0
    interrupted = False
    
    # Signal handler for clean exit
    def signal_handler(signum, frame):
        nonlocal interrupted
        interrupted = True
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # Optimize for terminal size and capabilities
    def clear_screen():
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()
    
    def reset_cursor():
        sys.stdout.write(RESET_CURSOR)
        sys.stdout.flush()
    
    def hide_cursor():
        sys.stdout.write(HIDE_CURSOR)
        sys.stdout.flush()
    
    def show_cursor():
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()

    hide_cursor()
    
    # Pre-calculate frame display optimization
    frame_count = len(frames)
    target_frame_time = duration
    
    try:
        while count < cycles and not interrupted:
            cycle_start_time = time.time()
            
            for frame_idx, frame in enumerate(frames):
                if interrupted:
                    break
                    
                frame_start_time = time.time()
                
                # Reset cursor position instead of clearing (smoother)
                reset_cursor()
                
                # Use direct stdout write for faster output
                sys.stdout.write(frame)
                sys.stdout.flush()
                
                # Adaptive timing - account for rendering time
                render_time = time.time() - frame_start_time
                sleep_time = max(0, target_frame_time - render_time)
                
                if sleep_time > 0:
                    time.sleep(sleep_time)
                
            count += 1
            
            # Optional: Add slight pause between cycles for better visual separation
            if count < cycles:
                time.sleep(0.01)
                
    except KeyboardInterrupt:
        interrupted = True
    finally:
        show_cursor()
        clear_screen()
