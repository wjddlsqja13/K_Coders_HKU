class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        water_level= []
        sum = 0
        
        #왼쪽과 오른쪽에서 가장 높은 bar의 높이를 각각 구한 후 
        #둘 중에 더 낮은 bar의 높이가 bar+water의 최대 높이
        for _ in range(1, len(height)-1,):
            left_max.append(max(height[0:_+1]))
            right_max.append(max(height[_:len(height)]))
        
        for _ in range(len(left_max)):
            water_level.append(min(left_max[_],right_max[_])-height[_+1])
        
        for i in water_level :
            sum += i
        
        return sum