#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for l in range(1, n):
        isSmallest = True
        v = arr[l]
        for i in range(l-1, -1, -1):
            if v <= arr[i]:
                arr[i+1] = arr[i]
            else:
                arr[i+1] = v
                isSmallest = False
                break
        if isSmallest: arr[0] = v
        
        for e in arr:
            print(e, end=" ")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
