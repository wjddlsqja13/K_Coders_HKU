#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    L = len(B)
    cache = [[0] * 2 for _ in range(L)]
    cache[0] = [0, 0]
    for i in range(1, L):
        cache[i][0] = max(cache[i-1][0], cache[i-1][1] + abs(B[i-1]-1))
        cache[i][1] = max(cache[i-1][0] + abs(B[i]-1), cache[i-1][1] + abs(B[i]-B[i-1]))

    return max(cache[L-1])
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
