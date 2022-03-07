#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    L = len(sticks)
    maxP = 0
    ans = [-1] * 3
    for i in range(L-2):
        for j in range(i+1, L-1):
            for k in range(j+1, L):
                if sticks[i] + sticks[j] <= sticks[k]:
                    break
                p = sticks[i] + sticks[j] + sticks[k]
                if p >= maxP:
                    maxP = p
                    ans = [sticks[i], sticks[j], sticks[k]]
    if ans[0] == -1:
        return [-1]
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
