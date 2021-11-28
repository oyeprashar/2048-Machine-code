import random 

class Board:
    def __init__(self,size,winningAmt):
        self.size = size
        self.winningAmt = winningAmt
        self.end = False

        self.grid = []

        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append(0)
            self.grid.append(row)

    def printBoard(self):
        for row in self.grid:
            print(row)

