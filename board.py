import numpy as np

from constants import *

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        #print(self.squares)
        
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0