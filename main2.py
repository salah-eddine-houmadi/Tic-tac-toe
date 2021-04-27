from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.title("Tic-Tac-Toe")
window.iconbitmap("tic.ico")


player =random.randint(1, 2)
if player == 1:
    messagebox.showinfo("1", "Player X :First")
else:
    messagebox.showinfo("2", "Player O :First")

comp = 0
def active(n):
    global comp
    global player
    comp += 1
    if n == 1 and player == 1 and b1["text"]=="":
        player = 2
        b1["text"] = "X"
    elif n == 1 and player == 2 and b1["text"]=="":
        player = 1
        b1["text"] = "O"
        player = 1
    #   #***
    elif n == 2 and player == 1 and b2["text"]=="" :
        player = 2
        b2["text"] = "X"
    elif n == 2 and player == 2 and b2["text"]=="":
        b2["text"] = "O"
        player = 1
        # ***
    elif n == 3 and player == 1 and b3["text"]=="":
        b3["text"] = "X"
        player = 2
    elif n == 3 and player == 2 and b3["text"]=="":
        b3["text"] = "O"
        player = 1
        # ***
    elif n == 4 and player == 1 and b4["text"] == "":
        b4["text"] = "X"
        player = 2
    elif n == 4 and player == 2 and b4["text"] == "":
        b4.config(text="O")
        player = 1
    # ***
    elif n == 5 and player == 1 and b5["text"] == "":
        b5["text"] = "X"
        player = 2
    elif n == 5 and player == 2 and b5["text"] == "":
        b5.config(text="O")
        player = 1
# ***
    elif n == 6 and player == 1 and b6["text"] == "":
        b6["text"] = "X"
        player = 2
    elif n == 6 and player == 2 and b6["text"] == "":
        b6["text"] = "O"
        player = 1
# ***
    elif n == 7 and player == 1 and b7["text"] == "":
        b7["text"] = "X"
        player = 2
    elif n == 7 and player == 2 and b7["text"] == "":
        b7["text"] = "O"
        player = 1
# ***
    elif n == 8 and player == 1 and b8["text"] == "":
        b8["text"] = "X"
        player = 2
    elif n == 8 and player == 2 and b8["text"] == "":
        b8["text"] = "O"
        player = 1
# ***
    elif n == 9 and player == 1 and b9["text"] == "":
        b9["text"] = "X"
        player = 2
    elif n == 9 and player == 2 and b9["text"] == "":
        b9["text"] = "O"
        player = 1
#     Analy
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"\
            or b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"\
             or b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo("Gagner", "Player 1 Est Gagne")
        exit(0)
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"\
            or b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"\
             or b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo("Gagner", "Player 1 Est Gagne")
        exit(0)
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"\
             or b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        messagebox.showinfo("Gagner", "Player 1 Est Gagne")
        exit(0)
#     O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O"\
            or b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"\
             or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo("Gagner", "Player 2 Est Gagne")
        exit(0)
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O"\
            or b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O"\
             or b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo("Gagner", "Player 2 Est Gagne")
        exit(0)
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O"\
             or b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        messagebox.showinfo("Gagner", "Player 2 Est Gagne")
        exit(0)
    elif comp == 9:
        messagebox.showinfo("Ta3adol", "Ta3adol")
        exit(0)


b1 = Button(window,text="",command = lambda:active(1),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b1.grid(row="0", column="0")
b2 = Button(window,text="",command = lambda:active(2),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b2.grid(row="0",column="1")
b3 = Button(window,text="",command = lambda:active(3),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b3.grid(row="0",column="2")
b4 = Button(window,text="",command = lambda:active(4),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b4.grid(row="1",column="0")
b5 = Button(window,text="",command = lambda:active(5),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b5.grid(row="1",column="1")
b6 = Button(window,text="",command = lambda:active(6),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b6.grid(row="1",column="2")
b7 = Button(window,text="",command = lambda:active(7),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b7.grid(row="2",column="0")
b8 = Button(window,text="",command = lambda:active(8),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b8.grid(row="2",column="1")
b9 = Button(window,text="",command = lambda:active(9),background="yellow",font=("Arial 30 bold"),width=4,height=2,borde=10)
b9.grid(row="2",column="2")


window.mainloop()