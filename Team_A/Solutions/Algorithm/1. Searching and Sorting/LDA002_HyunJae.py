class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element, n = 1, len(nums)
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                nums[element] = nums[i]
                element += 1
           
        
        return element
