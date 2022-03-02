class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        stack = [_ for _ in range(min(n,9),0,-1)]
        
        while stack :
            i = stack.pop()
            if i > n :
                continue
            else :
                result.append(i)
            for j in range(9,-1,-1):
                stack.append(i*10 + j)
        
        return result