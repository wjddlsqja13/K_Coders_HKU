class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        s = []
        for i in range(len(heights)-1, -1, -1):
            while s and heights[i] > s[-1]:
                s.pop()
                ans[i] += 1
            if s:
                ans[i] += 1
            s.append(heights[i])
        return ans