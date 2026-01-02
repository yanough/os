# library.py
import socket
import logging

log_file = "library_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO)

def log_event(event):
    logging.info(event)

def library_service(port, users, books):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(3)  # اجازه به 3 درخواست همزمان
    print(f"Library service is listening on port {port}...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        
        data = client_socket.recv(1024).decode()
        process_request(data, users, books)
        client_socket.send(b"Request processed.")
        client_socket.close()

def process_request(data, users, books):
    log_event(f"Processing request: {data}")
    command = data.split()
    
    if command[0] == "register_user":
        register_user(command[1], users)
    elif command[0] == "register_book":
        register_book(command[1], books)
    elif command[0] == "lend_book":
        lend_book(int(command[1]), command[2], users, books)
    elif command[0] == "return_book":
        return_book(int(command[1]), command[2], users, books)

def register_user(user_name, users):
    user_id = len(users) + 1
    users[user_id] = user_name
    log_event(f"User registered: {user_name} with ID {user_id}")
    return user_id

def register_book(book_title, books):
    books[book_title] = "available"
    log_event(f"Book registered: {book_title}")
    
def lend_book(user_id, book_title, users, books):
    if user_id not in users:
        log_event(f"User ID {user_id} not found.")
        return "failure"
    if book_title not in books or books[book_title] != "available":
        log_event(f"Book {book_title} not available.")
        return "failure"
    books[book_title] = "lent"
    log_event(f"Book {book_title} lent to user {user_id}.")
    return "success"

def return_book(user_id, book_title, users, books):
    if user_id not in users:
        log_event(f"User ID {user_id} not found.")
        return "failure"
    if book_title not in books or books[book_title] != "lent":
        log_event(f"Book {book_title} not lent.")
        return "failure"
    books[book_title] = "available"
    log_event(f"Book {book_title} returned by user {user_id}.")
    return "success"
