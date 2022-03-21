class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        return False
                    else:
                        stack = stack[:-1]
            return False if stack else True
            
        q = collections.deque([s])
        ans_len = -1
        ans = []
        d = {}
        while q:
            string = q.popleft()
            L = len(string)
            if string in d or L < ans_len:
                continue
            if isValid(string):
                if L > ans_len:
                    ans_len = L
                    ans = [string]
                elif L == ans_len:
                    ans.append(string)
                d[string] = True
                continue
            else:
                d[string] = False
            for i in range(L):
                if string[i] in '()':
                    q.append(string[:i]+string[i+1:])
        return ans