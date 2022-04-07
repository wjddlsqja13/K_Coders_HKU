class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = [[0] * n for _ in range(m)]
        
        cache[0][0] = 1
        for i in range(1, m):
            cache[i][0] = 1
        for i in range(1, n):
            cache[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i-1][j]+cache[i][j-1]
        
        return cache[m-1][n-1]