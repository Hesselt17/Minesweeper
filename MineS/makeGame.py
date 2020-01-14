'''
Created on Dec 19, 2019

@author: TommyHessel
'''

'''
1. Create 2D Array with bombs, no two spaces same bomb, save bomb spaces 
2. blank (0)-8 assign numerical values to the spaces adjacent + diagonal to bomb spaces 
3. Blackout entire board
4. Find the blank regions using recursive method
5. Collect all the blank regions into sets, put into a list 
'''
import random

class mine:
    def __init__(self):
        self.name = "M"
        
class space:
    def __init__(self, prox):
        self.prox = str(prox)
        
def adjDiag(point, mineField):
    
    aroundLoc = []
    aroundVal = []
    rows = len(mineField)
    cols = len(mineField[0])
    
    sRow = point[0]
    sCol = point[1]
    rowLowBound = sRow - 1
    rowUppBound = sRow + 2
    colLowBound = sCol - 1
    colUppBound = sCol + 2
    
    if sRow == 0:
        rowLowBound = 0
    if sRow > rows:
        rowUppBound = rows
        
    if sCol == 0:
        colLowBound = 0
    if sCol > cols:
        colUppBound = cols
    
    for r in range (rowLowBound, rowUppBound):
        for c in range (colLowBound, colUppBound):
            if (r >= 0 and r <=rows-1 and c >= 0 and c <= cols-1):
                aroundLoc.append((r,c))
                aroundVal.append(mineField[r][c])
    
    return (aroundLoc, aroundVal)
     
                
def numProx(tile, mineField):
    
    proxCtr = adjDiag(tile, mineField)[1].count("M")
    
    return proxCtr

def printField(field): 
    colDex = [i for i in range(len(field[0]))]
    cdStr = ''
    for c in colDex:
        cdStr = cdStr + '    ' + str(c)
    print ()
    print (cdStr)
       
    for r in range(len(field)):
        print (r, field[r])

def recurseBlank(mineField, r, c, setOpen, visited):
    """
    Purpose: Recursive method that collects all tiles (row,col) in the blank regions. 
    Return: A 2-tuple with [0] the set (setOpen) corresponding to all the tiles
            and [1] a list (visited) with all the visited tiles. 
    """
    
    rows = len(mineField)
    cols = len(mineField[0])
    
    if (mineField [r][c] == '0' and (r,c) not in visited):
        
        visited.append((r,c))
        
        if (len ({(r,c)} & setOpen) == 0):
            setOpen.add((r,c))
 
            sRow = r
            sCol = c
            rowLowBound = sRow - 1
            rowUppBound = sRow + 2
            colLowBound = sCol - 1
            colUppBound = sCol + 2
        
            if sRow == 0:
                rowLowBound = 0
            if sRow > rows:
                rowUppBound = rows
            
            if sCol == 0:
                colLowBound = 0
            if sCol > cols:
                colUppBound = cols
            
            for Ri in range (rowLowBound, rowUppBound):
                for Cj in range (colLowBound, colUppBound):
                    if (Ri >= 0 and Ri <=rows-1 and Cj >= 0 and Cj <= cols-1):
                        if mineField[Ri][Cj] == '0':
                            recurseBlank(mineField, Ri, Cj, setOpen, visited)
    
    return (setOpen, visited)

def collectBlanks(mineField):
    """
    Purpose: Collect all the blank regions in the field as sets (setOpen). 
    Return: A list (blanks). Inside are sets of blank regions (setOpen). 
    """
    
    temp = []
    blanks = []
    setOpen = set()
    visited = []
    rows = len(mineField)
    cols = len(mineField[0])
    
    for r in range(rows):
        for c in range (cols):
            if (mineField[r][c] == "0"):
                chk = [blankSet for blankSet in temp if len({(r,c)} & blankSet) > 0]
                if (len(chk) == 0):
                    recurseBlank(mineField, r, c, setOpen, visited)
                    temp.append(setOpen)
                    setOpen = set()
    
    for blankSet in temp:
        edgePts = set()
        for p in blankSet: 
            aroundLoc = adjDiag(p, mineField)[0]
            for p2 in aroundLoc:
                edgePts.add((p2[0],p2[1]))
        blankSet = blankSet | edgePts
        blanks.append(blankSet)
    
    return blanks
    
            
def makeFields():
    """
    Purpose: Create the minefield with player input (rows, cols, # of mines).
             Randomly places the mines in the field. 
    Return: A 4-tuple with [0] the minefield grid (list of lists), [1] display grid (''),
            blank regions (list of sets), and locations of the mines (list of tuples).   
    """
    rows, cols, numMines = 0, 0, 0
    
    while (rows <= 0 or rows > 23):
        rows = int (input ("Number of Rows: "))
    while (cols <= 0 or cols > 23):
        cols = int (input ("Number of Columns: "))
    while (numMines <= 0 or numMines > rows*cols):
        numMines = int (input ("Number of Mines: "))
    
    mineField = [["" for j in range(cols)] for i in range(rows)]
    
    mineLoc = []
    
    for _ in range(numMines):
        loc = (random.randint(0,rows-1), random.randint(0,cols-1))
        while (loc in mineLoc):
            loc = (random.randint(0,rows-1), random.randint(0,cols-1))
        mineLoc.append(loc)
    
    # (Rows, Col)
    
    for m in mineLoc:
        r = m[0]
        c = m[1] 
        mineField[r][c] = mine().name
    
    for r in range(rows):
        for c in range (cols):
            if mineField[r][c] != 'M':
                mineField[r][c] = space(numProx((r,c), mineField)).prox
    
    #printField(mineField)
    blanks = collectBlanks(mineField)
    
    return (mineField, blanks, mineLoc)
    
if __name__ == '__main__':   
    pass