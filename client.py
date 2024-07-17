import socket
import threading

# TODO: assign server output string values to each slot.

server = socket.socket()
port = 12345

server.connect(("10.0.0.35", port))

def send():
    while True:
        response = input()
        server.send(response.encode())

def recieve():
    while True:
        print(server.recv(1024).decode())

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()