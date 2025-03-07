import socket
import threading
from tkinter import *
from tkinter import messagebox

# TODO: IP address entry widget
# TODO: Client should either close or try to reconnect when disconnected from server.
# TODO: update individual buttons as needed, instead of all for each loop
# TODO: Split this back into a client.py and ui.py file.
# TODO: Rename draw_message to tie_message.

# connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server.connect(("10.0.0.35", port))

# sends encoded data to server
def send(response):
    if response != None:
        server.send(response.encode())

# Recieves server response and updates UI accordingly
def recieve():
    while True:
        try:
            response = server.recv(1024).decode()
            if "WIN" in response:
                if "WIN X" in response:
                    print("You win!")
                    victory_message()
                elif "WIN O" in response:
                    print("You lose!")
                    defeat_message()
                else:
                    print("Draw!")
                    draw_message()
            else:
                update_buttons(response)
        
        # TODO: show a message window and close game window
        except:
            server.close()
            print("Disconnected from server")
            break


# Updates the button text on UI
def update_buttons(progress):
    for i in range(0, 9):
        if progress[i] != "|":
            buttons[i].config(text=progress[i])
        else:
            buttons[i].config(text="")

# These three messages display a message box and send a string to the server indicating that they have been closed
def victory_message():
    messagebox.showinfo(title="Victory!", message="You won!")
    send("OK")
    
def defeat_message():
    messagebox.showinfo(title="Defeat!", message="You lost!")
    send("OK")

def draw_message():
    messagebox.showinfo(title="Draw!", message="It's a draw!")
    send("OK")


# Give the recieve function a thread so that it can always be listening for server responses
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()


#UI
root = Tk()
root.geometry("400x400")
root.title("TicTacToe")

row1 = Frame(root)
row2 = Frame(root)
row3 = Frame(root)

row1.pack(side=TOP)
row2.pack(side=TOP)
row3.pack(side=TOP)

button1 = Button(row1, text='', width=15, height=7, command=lambda : send("1,1"))
button2 = Button(row1, text='', width=15, height=7, command=lambda : send("1,2"))
button3 = Button(row1, text='', width=15, height=7, command=lambda : send("1,3"))
button4 = Button(row2, text='', width=15, height=7, command=lambda : send("2,1"))
button5 = Button(row2, text='', width=15, height=7, command=lambda : send("2,2"))
button6 = Button(row2, text='', width=15, height=7, command=lambda : send("2,3"))
button7 = Button(row3, text='', width=15, height=7, command=lambda : send("3,1"))
button8 = Button(row3, text='', width=15, height=7, command=lambda : send("3,2"))
button9 = Button(row3, text='', width=15, height=7, command=lambda : send("3,3"))

button1.pack(side=LEFT, anchor=N)
button2.pack(side=LEFT, anchor=N)
button3.pack(side=LEFT, anchor=NE)
button4.pack(side=LEFT, anchor=W)
button5.pack(side=LEFT, anchor=CENTER)
button6.pack(side=LEFT, anchor=E)
button7.pack(side=LEFT, anchor=SW)
button8.pack(side=LEFT, anchor=S)
button9.pack(side=LEFT, anchor=SE)

buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()