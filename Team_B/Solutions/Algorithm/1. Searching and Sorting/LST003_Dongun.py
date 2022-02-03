class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ls = [x for x in nums1[:m]]
        i, j = 0, 0
        while i<m or j<n:
            if i == m:
                nums1[i+j:m+n] = nums2[j:n]
                break
            if j == n:
                nums1[i+j:m+n] = ls[i:m]
                break
            if ls[i] < nums2[j]:
                nums1[i+j] = ls[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
            
#improved
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:              
            if m <= 0 or nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            
        