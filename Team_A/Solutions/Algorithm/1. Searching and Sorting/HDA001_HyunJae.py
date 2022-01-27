class Solution:
    def sumOfDigits (self, N):
        # code here
        N = list(str(N))
        addition = sum(list(map(int,N)))
        
        return addition