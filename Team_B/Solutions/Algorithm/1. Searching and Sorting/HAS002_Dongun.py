#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    ans = 0
    p = [a[0]] #prefix sum
    for i in range(1, len(a)):
        p.append(((a[i] % m)+p[i-1]) % m)
        ans = max(ans, p[i])
    if ans == m-1:
        return ans
    s = sorted((v, i) for i, v in enumerate(p)) #prefix sum sorted by val, idx
    print(s)
    for i in range(1, len(s)):          
        if s[i][1] < s[i-1][1]:
            v = (s[i-1][0] - s[i][0] + m) % m
            ans = max(ans, v)
            if ans == m-1: break
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
