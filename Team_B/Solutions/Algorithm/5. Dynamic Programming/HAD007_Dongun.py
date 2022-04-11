#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    MOD = 10 ** 9 + 7
    t = [0] * (m+1) # total ways
    g = [0] * (m+1) # good ways
    t[0], g[1] = 1, 1
    
    for i in range(1, m+1):
        t[i] += t[i-1] if i-1>=0 else 0
        t[i] += t[i-2] if i-2>=0 else 0
        t[i] += t[i-3] if i-3>=0 else 0
        t[i] += t[i-4] if i-4>=0 else 0
    for i in range(1, m+1):
        t[i] %= MOD
        t[i] **= n
        t[i] %= MOD
        
    for i in range(2, m+1):
        g[i] = t[i]
        for j in range(1, i):
            g[i] -= g[j] * t[i-j]
        g[i] %= MOD
        
    return g[m]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
