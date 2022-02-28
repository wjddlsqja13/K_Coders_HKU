class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            if i <= n:
                ans.append(i)
                ans.extend(self.getNextNum(i, n))
        return ans
        
    def getNextNum(self, n, maxN):
        if n * 10 > maxN:
            return []
        ret = []
        for i in '0123456789':
            cur = int(str(n) + i)
            if cur > maxN:
                continue
            else:
                ret.append(cur)
                ret.extend(self.getNextNum(cur, maxN))
        return ret