"""
0 denotes left
1 denotes right
2 denotes top
3 denotes bottom
"""

from board import Board 
from logic import Play

currBoard = Board(4,4)
playing = Play(currBoard)

playing.addRandomTile()
playing.addRandomTile()

currBoard.printBoard()

print("--------------------------------------------")

while currBoard.end != True:
    dir = int(input())
    playing.move(dir)
    currBoard.printBoard()
    print("--------------------------------------------")

