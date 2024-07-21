# Overview

This is a simple TicTacToe server and client application that I created to practice using sockets and threading in python. The server can just be ran from the terminal using python, but to use the client you'll need to change the local ip address to the one the host machine is using.

[Software Demo Video](https://youtu.be/mKeHsvf3gPo)
Since recording this, I have limited the sockets to INET and set them to create a TCP connection.

# Network Communication

Client/Server
TCP
Port: 12345
Data is sent using encoded strings

# Development Environment

* Python
* VsCode
* tkinter

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Threading](https://docs.python.org/3/library/threading.html)
* [Sockets](https://docs.python.org/3/howto/sockets.html)
* [tkinter](https://docs.python.org/3/library/tk.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* TODO: create a new instance of the game for each client
* TODO: Allow user to choose between ai and human opponent
* TODO: Users will connect to each other using unique passcodes
* TODO: Error messagebox when trying to connect to a non-existant or full session.
* TODO: Send client the coordinate and team value for each updated slot, instead of generating a string of team values.
* TODO: IP address entry widget
* TODO: Client should either close or try to reconnect when disconnected from server.
* TODO: update individual buttons as needed, instead of all for each loop
* TODO: FIX: opponent ai only checks for available slots in a single row.
This can lead to the opponent not selecting a slot during their turn.
* TODO: option to play with other players (remember to add a check before running ai-player select)