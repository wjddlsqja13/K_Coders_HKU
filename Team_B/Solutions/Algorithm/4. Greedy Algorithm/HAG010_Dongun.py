#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(n, p, x, m, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    towns = [[x1, p1] for x1, p1 in zip(x, p)]
    towns.sort()
    x = [t[0] for t in towns]
    
    sum = 0
    a = [0] * n
    preSum = [0] * (n+1) #store prefix sum
    for i in range(m): # for every cloud
        start = y[i]-r[i]
        end = y[i]+r[i]
        
        if end < towns[0][0] or start > towns[-1][0]: # if out of range, skip
            continue
            
        s = bisect.bisect_left(x, start) # start index in x
        e = bisect.bisect_right(x, end) - 1 # end index in x

        a[s] += 1
        if e < n-1: # if end within x
            a[e+1] -= 1 # only include before e
            
    for i in range(1, n):
        a[i] += a[i-1] # cloud count
        
    for i in range(n):
        if a[i] == 0: # if no cloud then add population to sum
            sum += towns[i][1]
        
    for i in range(1, n+1):
        if a[i-1] == 1: # if only 1 cloud then add to prefix sum
            preSum[i] = towns[i-1][1] + preSum[i-1]
        else:
            preSum[i] = preSum[i-1]       
    
    add = 0
    for i in range(m):
        start = y[i]-r[i]
        end = y[i]+r[i]
        
        if end < towns[0][0] or start > towns[-1][0]: # if out of range, skip
            continue
            
        s = bisect.bisect_left(x, start) # start index in x
        e = bisect.bisect_right(x, end) - 1 # end index in x
        add = max(preSum[e+1]-preSum[s], add)

    return sum + add
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(n, p, x, m, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
