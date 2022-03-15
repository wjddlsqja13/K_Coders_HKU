class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx = 0
        L = len(nums)
        for i in range(L):
            if i > mx: break
            mx = max(mx, nums[i] + i)
        return True if mx >= L-1 else False
    
        """
        # Works but slow
        
        L = len(nums)
        visited = [False] * L
        visited[0] = True
        for i in range(L-1):
            if visited[i]:
                for j in range(1, nums[i]+1):
                    if i+j == L-1:
                        return True
                    if i+j < L:
                        visited[i+j] = True
            
        return visited[L-1]
        """