class FreqStack:

    def __init__(self):
        self.count = collections.Counter()
        self.cntStack = collections.defaultdict(list)
        self.mxFreq = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] > self.mxFreq:
            self.mxFreq = self.count[val]
        self.cntStack[self.count[val]].append(val)

    def pop(self) -> int:
        ret = self.cntStack[self.mxFreq].pop()
        if len(self.cntStack[self.mxFreq]) == 0:
            self.mxFreq -= 1
        self.count[ret] -= 1
        return ret
        
    


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()