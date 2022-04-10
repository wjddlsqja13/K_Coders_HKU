#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    L = len(arr)
    sa_cache, ss_cache = [-sys.maxsize-1] * L, [[-sys.maxsize-1] * 2 for _ in range(L)]
    sa_cache[0], ss_cache[0] = arr[0], [arr[0], arr[0]]
    for i in range(1, L):
        sa_cache[i] = max(sa_cache[i-1]+arr[i], arr[i])
        ss_cache[i][0] = max(ss_cache[i-1][0], ss_cache[i-1][1], arr[i])
        ss_cache[i][1] = max(ss_cache[i-1][0]+arr[i], ss_cache[i-1][1]+arr[i])
    print(sa_cache, ss_cache)
    return [max(sa_cache), max(ss_cache[L-1])]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
