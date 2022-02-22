class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for n in nums:
            if n == 0: r += 1
            elif n == 1: w += 1
            else: b += 1
    
        nums[0:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:r+w+b] = [2] * b        