#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    #스택 이용해서 다시 풀어보기
    maxArea = 0
    for i in range(len(h)) : 
        length = 1
        j = i + 1
        k = i - 1
        
        while j != len(h) and h[j] >= h[i] :
            length += 1 
            j += 1
        
        while k >= 0 and h[k] >= h[i] :
            length += 1
            k -= 1
        
        area = length * h[i]
        
        if area > maxArea :
            maxArea = area    
              
    return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()