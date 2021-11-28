import random

class Play:
    def __init__(self,board):
        self.board = board
        self.maxScore = 2 
    
    def isWinner(self):
        n = self.board.size 
        for i in range(n):
            for j in range(n):
                self.maxScore = max(self.maxScore,self.board.grid[i][j])
            
        if self.maxScore == self.board.winningAmt:
            return True 
        else:
            return False

    def isFull(self):
        full = True 
        n = self.board.size 

        for i in range(n):
            for j in range(n):
                if self.board.grid[i][j] == 0:
                    full = False
                    break 
        
        return full
    
    def move(self,direction):
    

        if self.board.end == True or self.isFull() == True:
            print("Game over")
            self.board.end = True
            return 

        if direction == 0:
            self.moveLeft()
        
        elif direction == 1:
            self.moveRight()
        
        elif direction == 2:
            self.moveUp()
        
        elif direction == 3:
            self.moveDown()
        
        if self.isWinner() == True:
            print("Congratulations")
            self.board.end = True
            return 
        
        self.addRandomTile()
        
    def moveLeft(self):
        self.compress()
        self.merge()
        self.compress()
    
    def moveRight(self):
        self.reverse()
        self.moveLeft()
        self.reverse()
    
    def moveUp(self):
        self.transpose()
        self.moveLeft()
        self.transpose()
    
    def moveDown(self):
        self.transpose()
        self.moveRight()
        self.transpose()
        
    def compress(self):
        n = self.board.size 

        newMat = []
        for x in range(n):
            list1 = []
            for y in range(n):
                list1.append(0)
            newMat.append(list1)

        for i in range(n):
            pos = 0 
            for j in range(n):
                if self.board.grid[i][j] != 0:
                    newMat[i][pos] = self.board.grid[i][j]
                    pos += 1
                
        for i in range(n):
            for j in range(n):
                self.board.grid[i][j] = newMat[i][j]

    def merge(self):

        n = self.board.size 

        for i in range(n):
            for j in range(n-1):

                if self.board.grid[i][j] == self.board.grid[i][j+1]:
                    self.board.grid[i][j] *= 2 
                    self.board.grid[i][j+1] = 0
                
    def reverse(self):

        n = self.board.size 

        for i in range(n):
            self.board.grid[i] = self.board.grid[i][::-1]

    def transpose(self):
        n = self.board.size 
        starti = 0
        startj = 1

        while startj < n:
            i = starti 
            j = startj 

            while j < n:
                self.board.grid[i][j],self.board.grid[j][i] = self.board.grid[j][i],self.board.grid[i][j]
                i += 1
                j += 1
            
            startj += 1
        
    def addRandomTile(self):
        
        if self.isFull() == True:
            return 

        n = self.board.size 

        i = random.randint(0,n-1)
        j = random.randint(0,n-1)

        if self.board.grid[i][j] != 0:
            self.addRandonTile()
        
        self.board.grid[i][j] = 2
        





        

        

