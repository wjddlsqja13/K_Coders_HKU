#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    minimum = [1 for _ in range(len(arr))]
    for i in range(len(arr)-1) :
        if arr[i] < arr[i+1] :
            minimum[i+1] = minimum[i] +1
    
    for j in range(len(arr)-1,0,-1) :
        if arr[j-1] > arr[j] and minimum[j-1] <= minimum[j] :
            minimum[j-1] =minimum [j] +1

    return sum(minimum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
