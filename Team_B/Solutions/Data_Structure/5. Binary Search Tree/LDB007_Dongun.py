class Solution:       
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        m = [0] * (n+1)
        m[0], m[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(i):
                m[i] += m[j] * m[i-j-1]
        
        return m[n]