import socket
import threading
from grid import Grid

server = socket.socket()
port = 12345
server.bind(('', port))
print(f"Socket bound to {port}")
server.listen(5)
print("socket is listening")

grid = Grid()

def send():
    while True:
        response = input()
        client.send(response.encode())

def recieve():
    while True:
        response = client.recv(1024).decode()
        if response != "":  
            # convert response to tuple
            response = response.split(",")
            response = (int(response[0]), int(response[1]))

            print(response)
            grid.select_slot(response, 0)
            print(grid.slots)


# TODO: give each new connection a thread to allow for multiple connections and simultaneous games
while True:
    # socket.accept() returns (a new socket object, address)
    client, addr = server.accept()
    print(f"Got connection from {addr}")

    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()