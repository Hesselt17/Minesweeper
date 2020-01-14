'''
Created on Dec 20, 2019

@author: TommyHessel
'''

'''
1. Call makeGame to create the mineField with mines and blank regions
2. Run the GUI to keep track of game
'''

import makeGame, GUI

if __name__ == '__main__':
    
    fields = makeGame.makeFields()
    
    mineField = fields[0]
    blanks = fields[1]
    mineLoc = fields[2]
    
    ROWS = len(mineField)
    COLS = len(mineField[0])
    
    GUI.runGUI(mineField, blanks, mineLoc)
        
        
        