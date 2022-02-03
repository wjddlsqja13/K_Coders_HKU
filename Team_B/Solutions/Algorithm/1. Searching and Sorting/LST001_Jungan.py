class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1] :
                continue
            #pointer 사용
            left = i+1 
            right = len(nums)-1 
            while left < right :
                sum = nums[i] + nums[left] + nums[right]
                #sum이 0보다 작으면 더 큰 값 찾기
                if sum < 0 :
                    left += 1
                #sum이 0보다 크면 더 작은 값 찾기
                elif sum > 0 : 
                    right -= 1
                else : #sum == 0 
                    solution.append([nums[i],nums[left],nums[right]])

                    #중복인 경우
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                
        return solution
        