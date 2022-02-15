class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = 0
        final_nums = nums1 + nums2
        final_nums.sort()
        if len(final_nums) % 2 == 0:
            median_val = (final_nums[((m+n)//2)-1] + final_nums[((m+n)//2)])/2
        elif len(final_nums) % 2 == 1:
            median_val = (final_nums[(m+n)//2])
        return median_val
