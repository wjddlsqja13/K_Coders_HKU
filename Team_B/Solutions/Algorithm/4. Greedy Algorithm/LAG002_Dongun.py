class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict()
        ans = ""
        L = len(s)
        
        for i in range(L):
            d[s[i]] = i
        
        stack = collections.deque()
        for i in range(L):
            if s[i] in stack:
                continue
            if not stack or stack[-1] < s[i]:
                stack.append(s[i])
                continue
            if stack[-1] > s[i]:
                while stack and stack[-1] > s[i] and d[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])
        
        for c in stack:
            ans += c   
            
        return ans
