#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    v = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] >= v: 
            arr[i+1] = arr[i]
            for e in arr: print(e, end=" ")
            print()
        else: 
            arr[i+1] = v
            for e in arr: print(e, end=" ")
            print()
            return
    arr[0] = v
    for e in arr: print(e, end=" ")
    print()
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
