#dp solution, time limit exceeded
class Solution:
       
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = [0] * (len(envelopes))
        envelopes.sort()
        ans = 0
        for i in range(len(envelopes)):
            dp[i] = 1
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[j]+1, dp[i])
            ans = max(ans, dp[i])
        return ans

#dp + lis
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
        return len(dp)

