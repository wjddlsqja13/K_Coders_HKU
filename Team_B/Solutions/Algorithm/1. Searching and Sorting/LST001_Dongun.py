class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        ans = []
        nums.sort()
        while i < len(nums)-2:
            l = i + 1
            r = len(nums)-1
            while l < r:
                v = nums[i] + nums[l] + nums[r]
                if v == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                if v <= 0:
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                if v >= 0:
                    while r-1 > l and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                
            while i+1 < len(nums)-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans