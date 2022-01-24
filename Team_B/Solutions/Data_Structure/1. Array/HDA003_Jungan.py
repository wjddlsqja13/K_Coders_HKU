#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    result = []
    maximum = 0
    sum = 0
    
    for i in range(n+1) :
        result.append(0)
    
    #a에 k를 더해주고 b+1에 k를 빼주는 간단한 for loop
    for q in queries:
        result[q[0]-1] += q[2]
        result[q[1]] -= q[2]
    
    #변경된 array를 만들지 않고 sum을 이용하여 max를 구함으로서 계산을 최소화
    for i in range(n):
        sum += result[i]
        maximum = max(sum,maximum)
        
    return maximum

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
