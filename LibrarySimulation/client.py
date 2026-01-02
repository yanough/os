# client.py
import socket
import time

def user_request(command, port):
    time.sleep(2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', port))
        s.send(command.encode())
        response = s.recv(1024)
        print(f"Response from library: {response.decode()}")

if __name__ == "__main__":
    user_commands = [
        "register_user John_Doe",
        "register_book Harry_Potter",
        "lend_book 1 Harry_Potter",
        "return_book 1 Harry_Potter"
    ]
    
    port = 5000
    for cmd in user_commands:
        user_request(cmd, port)
