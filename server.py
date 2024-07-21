import socket
import threading
from grid import Grid

# TODO: create a new instance of the game for each client

# TODO: Allow user to choose between ai and human opponent
# TODO: Users will connect to each other using unique passcodes
# TODO: Error messagebox when trying to connect to a non-existant or full session.

# TODO: Send client the coordinate and team value for each updated slot, instead of generating a string of team values.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server.bind(('', port))
print(f"Socket bound to {port}")
server.listen(5)
print("socket is listening")

grid = Grid()

def recieve():
    while True:
        try:
            response = client.recv(1024).decode()
            if response != None:
                # Send team string when "OK" is recieved - indicating that a win/lose message box has been closed on the client's end.
                if "OK" in response:
                    send_progress()

                else:
                    # convert response to tuple for grid coordinates
                    response = response.split(",")
                    response = (int(response[0]), int(response[1]))

                    # try to assign the slot at (response) to O team
                    print(response)
                    grid.select_slot(response, 0)

                    # opponent's turn
                    grid.opponent()
                    send_progress()
                    is_game_over()
        except:
            client.close()
            break


# send client current grid progress X and O are teams, and | is an empty slot
def send_progress():
    print(grid.slots)
    client.send(grid.get_progress().encode())


# send victory/loss/draw to client (if found) and reset grid
def is_game_over():
    if grid.win != "":
        if grid.win == "X":
            client.send("WIN X".encode())
        elif grid.win == "O":
            client.send("WIN O".encode())
        else:
            client.send("WIN DRAW".encode())
        grid.reset()


# TODO: give each new connection a thread to allow for multiple connections and simultaneous games
while True:
    # socket.accept() returns (a new socket object, address)
    client, addr = server.accept()
    print(f"Got connection from {addr}")

    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()