#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    cs = [0] * 201
    m, m1, m2 = 0, 0, 0
    if d % 2 == 0:
        i1, i2 = (d-1)//2, (d-1)//2+1
    else:
        i1, i2 = (d-1)//2, (d-1)//2
    count = 0
    
    for i in range(len(expenditure)):
        if i < d:
            cs[expenditure[i]] += 1
            continue
        
        j, k = 0, 0

        while k <= i2:
            if k > i1:
                m2 = j
            else:
                m1 = j
                m2 = j
            k += cs[j]
            j += 1
        m = (m1 + m2) / 2

        if expenditure[i] >= m * 2:
            count += 1
        cs[expenditure[i-d]] -= 1
        cs[expenditure[i]] += 1
        
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
