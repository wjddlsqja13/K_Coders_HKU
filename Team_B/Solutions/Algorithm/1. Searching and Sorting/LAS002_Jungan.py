import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total_len = len(nums1) + len(nums2)
        mid = (total_len - 1) / 2 
        limit1 = min(math.ceil(mid)+1,len(nums1))
        limit2 = min(math.ceil(mid)+1,len(nums2))
        new_arr = sorted(nums1[:limit1] + nums2[:limit2])

        if (total_len - 1) % 2 != 0 :
            output = (new_arr[math.ceil(mid)] + new_arr[math.ceil(mid)-1]) /2
        else :
            output = new_arr[int(mid)]

        return output