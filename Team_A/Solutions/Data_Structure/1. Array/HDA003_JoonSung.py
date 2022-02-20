#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    for a, b, k in queries:
        for i in range(a-1, b):
            arr[i] += k
    return max(arr)
#Does not work on some conditions...need help 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
