class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        L = len(nums)
        ans  = 1
        tail = [0] * (L+1)
        tail[0] = nums[0]

        for i in range(1, L):
            if nums[i] > tail[ans-1]:
                tail[ans] = nums[i]
                ans += 1
            else:
                tail[bisect_left(tail, nums[i], 0, ans-1)] = nums[i]

        return ans