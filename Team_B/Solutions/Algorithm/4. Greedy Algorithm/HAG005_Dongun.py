#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    L = len(arr)
    
    d1 = dict(enumerate(arr))           # idx: val
    d2 = {v: k for k, v in d1.items()}  # val: idx
    
    for i in range(L):
        if k:
            if d1[i] != L-i:
                i1, v1 = d2[d1[i]], d1[i]
                i2, v2 = d2[L-i], d1[d2[L-i]]
                d1[i1], d1[i2] = v2, v1
                d2[v1], d2[v2] = i2, i1
                k -= 1    
        else: break
        
    ans = [0] * L
    for k, v in d1.items():
        ans[k] = v
        
    return ans
            
    
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
