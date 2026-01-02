# server.py
import socket
import multiprocessing
from library import library_service

if __name__ == "__main__":
    port = 5000
    users = {}
    books = {}
    
    # راه‌اندازی پردازه کتابخانه
    library_process = multiprocessing.Process(target=library_service, args=(port, users, books))
    library_process.start()
    library_process.join()
