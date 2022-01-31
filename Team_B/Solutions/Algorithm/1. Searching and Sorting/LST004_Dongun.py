#brute force, time limit exceeded
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # pick one from each list
        # set range as [min, max] from lists
        # update shortest if shortest > len(range)
        pos = [0] * len(nums)
        maxN = -100001
        ans = [-100001, 100001]
        
        while True:
            minPos = -1
            minN = 100001

            for i in range(len(nums)):
                n = nums[i][pos[i]]             
                if n < minN:
                    minN = n
                    minPos = i
                if n > maxN:
                    maxN = n

            if maxN - minN < ans[1] - ans[0]:
                ans = [minN, maxN]
            if ans[1] - ans[0] == 0: return ans
            if pos[minPos] == len(nums[minPos])-1: return ans
            else: pos[minPos]+=1

#sliding window solution
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        d, res = [], []
        K = len(nums)
        count = collections.defaultdict(int)
        # make nums into a list of [val, idx]
        for i, num in enumerate(nums):
            for n in num:
                d.append([n, i])
        d.sort(key=lambda x: x[0])
        left = 0
        
        for right, n in enumerate(d):
            count[n[1]] += 1
            
            # while the range has numbers from all sublist
            while len(count)==K:
                if not res or d[right][0]-d[left][0]<res[1]-res[0]:
                    res = [d[left][0], d[right][0]]
                    
                count[d[left][1]] -= 1
                if count[d[left][1]]==0:
                    count.pop(d[left][1])
                    
                left += 1
        return res