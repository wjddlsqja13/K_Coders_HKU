class Solution:
    def trap(self, height: List[int]) -> int:
        left_i = 0
        left = height[left_i]
        right = height[-1]
        right_i = len(height)-1
        rain = 0
        while left_i < right_i: 
            if left < right:
                left_i = left_i + 1
                if height[left_i] < left:
                    rain = rain + left - height[left_i]
                else:
                    left = height[left_i]
            else:
                right_i = right_i - 1
                if height[right_i] < right:
                    rain = rain + right - height[right_i]
                else:
                    right = height[right_i]                
        return rain