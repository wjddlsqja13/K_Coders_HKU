#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(l):
    sort = sorted(l)
    rev = list(reversed(l))

    d = {k: v for v, k in enumerate(sort)}

    swaps = countSwap(d, l, sort)

    d = {k: v for v, k in enumerate(sort)}

    swaps_rev = countSwap(d, rev, sort)

    return min(swaps, swaps_rev)

def countSwap(d, a, s):
    swap = 0
    i = 0
    
    while i < len(a):
        if a[i] != s[i]:
            swap += 1
            a[d[a[i]]], a[i] = a[i], a[d[a[i]]]
            continue
        i += 1
        
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
