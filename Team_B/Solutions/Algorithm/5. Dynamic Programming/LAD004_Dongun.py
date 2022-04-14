class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)
        c = [False] * (L+1)
        c[0] = True
        
        for i in range(1, L+1):
            for j in range(i, -1, -1):
                if c[j]:
                    sub = s[j:i]
                    if sub in wordDict:
                        c[i] = True
                        break
                        
        return c[L]