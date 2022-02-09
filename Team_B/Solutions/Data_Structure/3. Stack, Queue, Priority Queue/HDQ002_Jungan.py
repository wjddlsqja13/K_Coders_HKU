class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        smallest = s
        #if k == 1, recurse and find the lexicographically smallest string
        if k == 1: 
            for i in range(len(s)) :
                current = s[i:] + s[:i]
                if current < smallest :
                    smallest = current
        #if k >=2 , the lexicographically smallest string is the sorted string
        else : 
            smallest = "".join(sorted(s))
         
        return smallest