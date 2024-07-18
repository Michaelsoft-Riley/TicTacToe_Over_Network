import socket
import threading

# TODO: assign server output string values to each slot.

server = socket.socket()
port = 12345

server.connect(("10.0.0.26", port))

def send(response):
    if response != None:
        server.send(response.encode())

def recieve():
    while True:
        print(server.recv(1024).decode())

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()