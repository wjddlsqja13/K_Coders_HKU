#GDA001_JoonSung
class Solution:
    def sumOfDigits (self, N):
        n=0
        for i in str(N):
            n=n+int(i)
        return(n)