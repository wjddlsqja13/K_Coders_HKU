class Solution:
    def trap(self, height: List[int]) -> int:
      
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        
        for i in range(1,n-1):
            left_max[i] = max(left_max[i-1],height[i])
            right_max[n-1-i] = max(right_max[n-i],height[n-1-i])
            
        answer = 0        
        for j in range(1,n-1):
            if left_max[j]>height[j] and right_max[j]>height[j]:
                answer += (min(left_max[j],right_max[j]) - height[j])
        
        return answer
