#Tic Tac Toe with GUI using Tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# X starts -> X = True and O = False
isClicked = True
count = 0

###Functions
#Disable all the buttons
def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#Check Win Condition
def checkWin():
    global winner
    winner = False


###Check for X's Wins
    #First Row X
    if b1["text"] != " " and b1["text"] == b2["text"] and b2["text"] == b3["text"]:
        b1.configure(highlightbackground="red")
        b2.configure(highlightbackground="red")
        b3.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b1["text"] +  " is the Winner!")
        disableAllButtons()

   #Second Row
    elif b4["text"] != " " and b4["text"] == b5["text"] and b5["text"] == b6["text"]:
        b4.configure(highlightbackground="red")
        b5.configure(highlightbackground="red")
        b6.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b4["text"] +  " is the Winner!")
        disableAllButtons()

    #Third Row
    elif b7["text"] != " " and b7["text"] == b8["text"] and b8["text"] == b9["text"]:
        b7.configure(highlightbackground="red")
        b8.configure(highlightbackground="red")
        b9.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b7["text"] +  " is the Winner!")
        disableAllButtons()

    #First Column
    elif b1["text"] != " " and b1["text"] == b4["text"] and b4["text"] == b7["text"]:
        b1.configure(highlightbackground="red")
        b4.configure(highlightbackground="red")
        b7.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b1["text"] +  " is the Winner!")
        disableAllButtons()

    #Second Column
    elif b2["text"] != " " and b2["text"] == b5["text"] and b5["text"] == b8["text"]:
        b2.configure(highlightbackground="red")
        b5.configure(highlightbackground="red")
        b8.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b2["text"] +  " is the Winner!")
        disableAllButtons()

    #Third Column
    elif b3["text"] != " " and b3["text"] == b6["text"] and b6["text"] == b9["text"]:
        b3.configure(highlightbackground="red")
        b6.configure(highlightbackground="red")
        b9.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b3["text"] +  " is the Winner!")
        disableAllButtons()
    
    #Top Left to Bottom Right Diagonal
    elif b1["text"] != " " and b1["text"] == b5["text"] and b5["text"] == b9["text"]:
        b1.configure(highlightbackground="red")
        b5.configure(highlightbackground="red")
        b9.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b1["text"] +  " is the Winner!")
        disableAllButtons()

    #Bottom Left to Top Right Diagonal
    elif b3["text"] != " " and b3["text"] == b5["text"] and b5["text"] == b7["text"]:
        b3.configure(highlightbackground="red")
        b5.configure(highlightbackground="red")
        b7.configure(highlightbackground="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", b3["text"] +  " is the Winner!")
        disableAllButtons()    

    #Check if Tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        disableAllButtons()

#Button clicked function
def buttonClick(b):
    global isClicked, count
    
    #Grabbing text with brackets, change to a player X or O, set isClicked, add to count
    if b["text"] == " " and isClicked == True:
        b["text"] = "X"
        isClicked = False
        count += 1
        checkWin()
    elif b["text"] == " " and isClicked == False:
        b["text"] = "O"
        isClicked = True
        count += 1
        checkWin()
    else:
        messagebox.showerror("Tic Tac Toe", "Box Already Selected\nPick Another Box")    

#Make/Reset the Board
def resetBoard():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global isClicked, count
    isClicked = True
    count = 0

    #Make Buttons
    b1 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b1))
    b2 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b2))
    b3 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b3))
    b4 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b4))
    b5 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b5))
    b6 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b6))
    b7 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b7))
    b8 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b8))
    b9 = Button(root, text = " ", font = ("Helventica", 20), height = 3, width = 6, highlightbackground = "White", command = lambda: buttonClick(b9))

    #Make Grid with Buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Create Menu
myMenu = Menu(root)
root.config(menu=myMenu)

#Create Options Menu
optionsMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=optionsMenu)
optionsMenu.add_command(label="Play Again", command = resetBoard)

resetBoard()

root.mainloop()
