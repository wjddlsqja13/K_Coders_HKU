class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dp(i, j):
            if not cache[i][j]:
                v = matrix[i][j]
                cache[i][j] = 1 + max(
                    dp(i-1, j) if i and matrix[i-1][j] > v else 0,
                    dp(i+1, j) if i < N-1 and matrix[i+1][j] > v else 0,
                    dp(i, j-1) if j and matrix[i][j-1] > v else 0,
                    dp(i, j+1) if j < M-1 and matrix[i][j+1] > v else 0)
            return cache[i][j]
                
        N = len(matrix)
        M = len(matrix[0])
        cache = [[0] * M for _ in range(N)]
        return max(dp(i, j) for i in range(N) for j in range(M))       