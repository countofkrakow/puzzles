import math
# Solves a given n x n sudoku board where n is a perfect square

class sudokuSolver:
    def __init__(self, board):
        self.board = board
        self.n = int(math.sqrt(len(self.board))) # length of grid square
        self.nn = int(len(self.board))         # length of grid

    def solve(self):
        if self.solve_private(0, 0):
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board]))
        else:
            print ("no possible answer")

    def solve_private(self, x, y):
        # finished with board
        if y >= self.nn:
            return True

        if (x >= self.nn - 1): # next row
            nX = 0
            nY = y + 1
        else:                  # next cell in same row
            nX = x + 1
            nY = y

        if (self.board[x][y] > 0): # preplaced number
            return self.solve_private(nX, nY)

        for i in range(1, self.nn + 1):
            if self.validMove(i, x, y):
                # place number
                self.board[x][y] = i
                if self.solve_private(nX, nY):
                    return True
                else: # remove number
                    self.board[x][y] = -1
        return False

    def validMove(self, val, x, y):
        # check column
        for cell in self.board[x]:
            if cell == val:
                return False

        # check row
        for i in range(self.nn):
            if self.board[i][y] == val:
                return False

        # check grid box
        minX = (x // self.n) * self.n
        minY = (y // self.n) * self.n
        for i in range(minX, minX + self.n):
            for j in range(minY, minY + self.n):
                if self.board[i][j] == val:
                    return False

        return True

if __name__ == "__main__":
    a = sudokuSolver([
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 4, 3, 0],
        [4, 0, 0, 3, 2, 1, 9, 7, 0],
        [1, 4, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 8, 3],
        [0, 5, 6, 7, 4, 8, 0, 0, 9],
        [0, 3, 7, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0]
                      ])
    a.solve()