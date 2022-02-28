from collections import deque
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        units = []
        if k > 1:
            return ''.join(sorted(s))
        else:
            for i in range(len(s)):
                unit = s[i:] + s[:i]
                units.append(unit)
            return min(units)
