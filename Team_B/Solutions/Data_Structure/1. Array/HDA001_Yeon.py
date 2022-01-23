#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here\
    # Write your code here
    results = []
    n = 6
    for i in range(n):
        for j in range(n):
            result = 0
            if i-1<n-1 or i+1>5 or j-1<0 or j+1>n-1:
                continue
            else:
                result = sum(arr[i-1][j-1:j+2]) + arr[i][j] + sum(arr[i+1][j-1:j+2])
                results.append(result)
    return max(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
