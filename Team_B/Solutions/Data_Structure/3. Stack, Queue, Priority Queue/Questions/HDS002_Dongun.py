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
    # Write your code here
    s = []
    i, ans = 0, 0
    
    while i < len(h):
        # if h[i] is equal to or greater than the top, push i into stack
        if len(s) == 0 or h[s[-1]] <= h[i]:
            s.append(i)
            i += 1
        # if h[i] is smaller than the top, pop i as the min height idx,
        # s[-1] is left, i-1 is right
        else:
            top = s.pop()
            if len(s) > 0:
                area = h[top] * (i-1 - s[-1])
            else:
                area = h[top] * i
            ans = max(area, ans)
        
    while len(s) > 0 :
        top = s.pop()
        if len(s) > 0:
            area = h[top] * (i-1 - s[-1])
        else:
            area = h[top] * i
        ans = max(area, ans)
    
    return ans
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
