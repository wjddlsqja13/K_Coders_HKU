class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        currentGas = 0
        totalGas = 0
        for i in range(len(gas)):
            totalGas += gas[i]-cost[i]
            currentGas += gas[i]-cost[i]
            if currentGas < 0:
                start = i + 1
                currentGas = 0
        return -1 if totalGas < 0 else start
