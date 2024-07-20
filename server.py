import socket
import threading
from grid import Grid

# TODO: only send the client the coordinate and team value for each updated slot

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
        if response != None:  
            # convert response to tuple
            response = response.split(",")
            response = (int(response[0]), int(response[1]))

            # accept client slot selection
            print(response)
            grid.select_slot(response, 0)

            # opponent's turn
            grid.opponent()

            # send client current grid progress
            print(grid.slots)
            client.send(grid.get_progress().encode())

            # if win, send victory to client and reset grid
            if grid.win != "":
                if grid.win == "X":
                    client.send("WIN X".encode())
                elif grid.win == "O":
                    client.send("WIN O".encode())
                else:
                    client.send("WIN DRAW".encode())
                grid.reset()

                # send client current grid progress
                print(grid.slots)
                client.send(grid.get_progress().encode())



# TODO: give each new connection a thread to allow for multiple connections and simultaneous games
while True:
    # socket.accept() returns (a new socket object, address)
    client, addr = server.accept()
    print(f"Got connection from {addr}")

    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()