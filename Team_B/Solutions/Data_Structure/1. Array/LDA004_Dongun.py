class Solution(object):
    def __init__(self):
        self.ans = []     

    def checkVertical(self, board, r, c, n):
        for i in range(n):
            if i == r:
                continue
            if board[i][c] == 'Q':
                return False
        return True
    
    def checkDiagonal(self, board, r, c, n):
        for i in range(1, n):
            if r-i >= 0 and c-i >= 0:
                if board[r-i][c-i] == 'Q':
                    return False
            if r+i < n and c-i >= 0:
                if board[r+i][c-i] == 'Q':
                    return False
            if r-i >= 0 and c+i < n:
                if board[r-i][c+i] == 'Q':
                    return False
            if r+i < n and c+i < n:
                if board[r+i][c+i] == 'Q':
                    return False
        return True
    
    def placeQueen(self, board, n, q):
        if q == n:
            self.ans.append(list(board))
            return
        
        for i in range(n):
            board[q] = board[q][:i] + 'Q' + board[q][i+1:n]

            if self.checkVertical(board, q, i, n) and self.checkDiagonal(board, q, i, n):
                self.placeQueen(board, n, q+1)
                
            board[q] = board[q][:i] + '.' + board[q][i+1:n]

        return
            
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = ['.' * n] * n
        self.placeQueen(board, n, 0)
        return self.ans
        
        
    
            
        
    
                
        