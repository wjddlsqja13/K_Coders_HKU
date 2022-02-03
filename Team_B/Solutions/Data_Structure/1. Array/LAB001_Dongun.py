class Solution:
    def __init__(self):
        self.emptyPos = []
        self.row = [[False] * 10 for _ in range(9)]
        self.col = [[False] * 10 for _ in range(9)]
        self.sqr = [[False] * 10 for _ in range(9)]
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.row[i][int(board[i][j])] = True
                    self.col[j][int(board[i][j])] = True
                    self.sqr[self.getSRange(i, j)][int(board[i][j])] = True
                else:
                    self.emptyPos.append([i, j])
        self.solve(len(self.emptyPos), board)
        
        
    
    def solve(self, n, board):
        if n == 0:
            return True
        for i, j in self.emptyPos:
            if board[i][j] == ".":
                for k in range(1, 10):
                    if not self.row[i][k] and not self.col[j][k] and not self.sqr[self.getSRange(i, j)][k]:
                        board[i][j] = str(k)
                        self.row[i][k], self.col[j][k], self.sqr[self.getSRange(i, j)][k] = True, True, True
                        if self.solve(n-1, board):
                            return True
                        board[i][j] = "."
                        self.row[i][k], self.col[j][k], self.sqr[self.getSRange(i, j)][k] = False, False, False
                return False
        return False
    
    def getSRange(self, i, j):
        return i//3*3 + j//3