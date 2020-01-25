'''
Created on Dec 21, 2019

@author: TommyHessel
'''

# from tkinter import Button, Frame, Menu, PhotoImage, Tk
from tkinter import *
import os

global ROWS, COLS, mineField, guiField, flagged, blanks, mineLoc, revealed
# [ R0[c0, c1, c2],  R1[c0, c1, c2]... ]

def controls():
    print ("show")
    return 0

def restart():
    print ("restart")
    python = sys.executable
    os.execl(python, python, *sys.argv)

root = Tk()
root.title('Minesweeper')
m = Frame(root)
m.grid(row=0)
butt = Button(m, text="Restart", command= restart)
butt2 = Button(m, text="Controls", command= controls)
butt3 = Button(m, text="Quit", command=quit)
butt.grid(row=0, column=0, padx=40)
butt2.grid(row=0, column=1, padx=40)
butt3.grid(row=0, column=2, padx=40)
f = Frame(root)
f.grid(row=1, padx=20, pady=20)

imgB = PhotoImage(file="pics/blank.png")
imgF = PhotoImage(file="pics/flag.png")
imgM, imgMexp = PhotoImage(file="pics/mine.png"), PhotoImage(file="pics/mine2.png")

numbersLst = [PhotoImage(file="pics/0.png"), PhotoImage(file="pics/1.png"),
              PhotoImage(file="pics/2.png"), PhotoImage(file="pics/3.png"),
              PhotoImage(file="pics/4.png"), PhotoImage(file="pics/5.png"),
              PhotoImage(file="pics/6.png"), PhotoImage(file="pics/7.png"),
              PhotoImage(file="pics/8.png")]

def runGUI(Mfield, blnks, mLoc):
    global ROWS, COLS, mineField, guiField, flagged, blanks, mineLoc, revealed

    mineField = Mfield
    blanks = blnks
    mineLoc = mLoc

    guiField = []
    flagged = []
    revealed = set()

    ROWS = len(mineField)
    COLS = len(mineField[0])

    for i in range(ROWS):
        ri = []
        for j in range(COLS):
            tile = Button(f, image=imgB, width=25, height=25)
            tile.grid(row=i, column=j)
            tile.bind('<Button-1>', clkTile)  # left click
            tile.bind('<Button-2>', flag)  # trackpad right click
            tile.bind('<Button-3>', flag)  # right mouse right click
            ri.append(tile)
        guiField.append(ri)

    root.mainloop()


def getPos(event):
    rowWin = event.y_root - f.winfo_rooty()
    colWin = event.x_root - f.winfo_rootx()
    pos = f.grid_location(rowWin, colWin)
    r, c = pos[0], pos[1]
    return (r, c)


def flag(event):
    global guiField, flagged
    modified = False
    pos = getPos(event)
    r, c = pos[0], pos[1]

    if (pos not in revealed):
        if (pos not in flagged and not modified):
            flagged.append(pos)
            modified = True
            guiField[r][c] = Button(f, image=imgF, width=25, height=25)

        if (pos in flagged and not modified):
            flagged.remove(pos)
            modified = True
            guiField[r][c] = Button(f, image=imgB, width=25, height=25)

        guiField[r][c].grid(row=r, column=c)
        guiField[r][c].bind('<Button-1>', clkTile)
        guiField[r][c].bind('<Button-2>', flag)
        guiField[r][c].bind('<Button-3>', flag)


def clkTile(event):
    global mineField, blanks, revealed
    pos = getPos(event)
    r = pos[0]
    c = pos[1]

    val = mineField[r][c]

    if (val == '0'):
        for s in blanks:
            if (len({(r, c)} & s) > 0):
                for tile in s:
                    val = mineField[tile[0]][tile[1]]
                    revealed.add(tile)
                    revealTile(tile[0], tile[1], val)
    elif (val != 'M'):
        revealed.add((r, c))
        revealTile(r, c, val)
    else:
        revealed.add((r, c))
        guiField[r][c] = Button(f, image=imgMexp, width=25, height=25)
        guiField[r][c].grid(row=r, column=c)

    checkGame(r, c)


def revealTile(r, c, val):
    global guiField

    if (val == 'M'):
        guiField[r][c] = Button(f, image=imgM, width=25, height=25)
        guiField[r][c].grid(row=r, column=c)
    else:
        for i in range(9):
            if (str(i) == val):
                guiField[r][c] = Button(f, image=numbersLst[i], width=25, height=25)
                guiField[r][c].grid(row=r, column=c)
                break


def revealAll():
    global mineField, guiField, revealed, ROWS, COLS

    for r in range(ROWS):
        for c in range(COLS):
            if len({(r, c)} & revealed) == 0:
                revealTile(r, c, mineField[r][c])


def checkGame(r, c):
    global ROWS, COLS, mineField, revealed, mineLoc

    if (mineField[r][c] == "M"):
        gameOver = True
        print("You Lost! Mine Hit!")
        revealAll()
        return gameOver

    if ((ROWS * COLS) - len(revealed) == len(mineLoc)):
        gameOver = True
        print("You Won! All Mines Swept!")
        revealAll()
        return gameOver


if __name__ == '__main__':
    pass
