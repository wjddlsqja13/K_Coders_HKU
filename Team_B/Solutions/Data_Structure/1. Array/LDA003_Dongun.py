class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water, lmax, rmax, left = 0, 0, 0, 0
        right = len(height)-1
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= lmax:
                    lmax = height[left]
                else:
                    water += lmax-height[left]
                left += 1           
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                else:
                    water += rmax-height[right]
                right -= 1
        return water
                    
            