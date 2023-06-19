from typing import List

class Solution:

    totalMatrix = 9

    def solveSudoku(self, board: List[List[str]]) -> None:
        emptyPosition = [0, 0]

        if (not self.findEmptyPosition(board, emptyPosition)):
            return True
        
        x, y = emptyPosition
        
        for number in range(1, 10):
            number = str(number)

            if self.locationIsValid(board, x, y, number):

                board[x][y] = number

                if (self.solveSudoku(board)):
                    return True
            
                board[x][y] = "."
        return False
    
    def findEmptyPosition(self, board: List[List[str]], emptyPosition: List) -> bool:
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    emptyPosition[0] = x
                    emptyPosition[1] = y
                    return True
        return False

    def locationIsValid(self, board: List[List[str]], x: int, y: int, number: str):
        return (not self.usedInRow(board, x, number) and
                not self.usedInColumn(board, y, number) and
                not self.usedInSquare(board, x, y, number))
  
    def usedInSquare(self, board: List[List[int]], x: int, y: int, number: str):
        leftX, leftY = 0, 0
        rigthX, rigthY = 0, 0
        if (x + 1)  % 3 == 0 :
            rigthX = x + 1
        else:
            rigthX = (x + 1) + (3 - (x + 1) % 3)

        if (y + 1) % 3 == 0:
            rigthY = y + 1
        else:
            rigthY = (y + 1) + (3 - ((y + 1) % 3))

        leftX, leftY = rigthX - 3, rigthY - 3
        return True in [number in board[row][leftY: rigthY] for row in range(leftX, rigthX)]
    
    def usedInRow(self, board: List[List[int]], x: int, number: str):
        return number in [board[x][row] for row in range(9)]

    def usedInColumn(self, board: List[List[int]], y: int, number: str):
        return number in [row[y] for row in board]