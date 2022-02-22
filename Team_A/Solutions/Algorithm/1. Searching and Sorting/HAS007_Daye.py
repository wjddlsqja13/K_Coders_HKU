#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):    
    i = 0
    pivot = arr[0]
    left = []
    equal = []
    right = []
    while i < len(arr):
        if arr[i] < pivot:
            left.append(arr[i])
            i+=1
        elif arr[i] == pivot:
            equal.append(arr[i])
            i+=1
        elif arr[i] > pivot:
            right.append(arr[i])
            i+=1

            
    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
