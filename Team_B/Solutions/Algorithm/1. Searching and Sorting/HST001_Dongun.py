#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    diff = sys.maxsize
    ans = []
    for i in range(len(arr)-1):
        if diff > arr[i+1] - arr[i]:
            diff = arr[i+1] - arr[i]
            ans = [arr[i], arr[i+1]]
        elif diff == arr[i+1] - arr[i]:
            ans.append(arr[i])
            ans.append(arr[i+1])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
