class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(n):
            if n in cache:
                return cache[n]
            if n % 2 == 0:
                cache[n] = 1 + dp(n//2)
                return cache[n]
            else:
                cache[n] = 1 + min(dp(n-1), dp(n+1))
                return cache[n]

        cache = {1:0}
        
        return dp(n)