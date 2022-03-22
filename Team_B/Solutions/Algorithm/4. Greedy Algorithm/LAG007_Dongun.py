class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """       
        L = len(wage)
        ratio = [(float(wage[i])/quality[i], quality[i]) for i in range(L)]
        ratio.sort()

        heap = []
        total_quantity = 0
        min_val = sys.maxsize
        for r, q in ratio:
            heapq.heappush(heap, -q)
            total_quantity += q
            if len(heap) > k:
                total_quantity += heapq.heappop(heap)
            if len(heap) == k:
                min_val = min(min_val, total_quantity*r)
        return min_val
        