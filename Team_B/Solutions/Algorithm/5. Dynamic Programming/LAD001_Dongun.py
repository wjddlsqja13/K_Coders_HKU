class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def addToParenthesis(p, l, num_open, num_close):
            if l == n*2:
                ans.append(p)
            else:
                if num_open > 0:
                    addToParenthesis(p+'(', l+1, num_open-1, num_close)
                if num_close > num_open:
                    addToParenthesis(p+')', l+1, num_open, num_close-1)
                    
        num_open, num_close = n, n
        addToParenthesis('(', 1, n-1, n)
        return ans