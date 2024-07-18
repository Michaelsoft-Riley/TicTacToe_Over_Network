import grid
import client
from tkinter import *

grid = Grid()

root = Tk()
root.geometry("400x400")
root.title("TicTacToe")

row1 = Frame(root)
row2 = Frame(root)
row3 = Frame(root)

row1.pack(side=TOP)
row2.pack(side=TOP)
row3.pack(side=TOP)

# TODO: The text for these should start blank and be filled with the team letter as slots are assigned in grid.
button1 = Button(row1, text='1', command=lambda : client.send("1,1"))
button2 = Button(row1, text='2', command=lambda : client.send("1,2"))
button3 = Button(row1, text='3', command=lambda : client.send("1,3"))
button4 = Button(row2, text='4', command=lambda : client.send("2,1"))
button5 = Button(row2, text='5', command=lambda : client.send("2,2"))
button6 = Button(row2, text='6', command=lambda : client.send("2,3"))
button7 = Button(row3, text='7', command=lambda : client.send("3,1"))
button8 = Button(row3, text='8', command=lambda : client.send("3,2"))
button9 = Button(row3, text='9', command=lambda : client.send("3,3"))

button1.pack(side=LEFT, anchor=N)
button2.pack(side=LEFT, anchor=N)
button3.pack(side=LEFT, anchor=NE)
button4.pack(side=LEFT, anchor=W)
button5.pack(side=LEFT, anchor=CENTER)
button6.pack(side=LEFT, anchor=E)
button7.pack(side=LEFT, anchor=SW)
button8.pack(side=LEFT, anchor=S)
button9.pack(side=LEFT, anchor=SE)

root.mainloop()