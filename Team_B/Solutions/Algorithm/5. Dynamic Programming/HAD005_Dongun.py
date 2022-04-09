#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(A, B):
    # Write your code here          
    al, bl = len(A), len(B)
    cache = [[False] * (bl+1) for _ in range(al+1)]
    cache[0][0] = True
    
    for i in range(al+1):
        for j in range(bl+1):
            if i != 0 and j == 0:
                cache[i][j] = a[i-1].islower() and cache[i-1][j]
            elif i != 0 and j != 0:
                if a[i-1] == b[j-1]:
                    cache[i][j] = cache[i-1][j-1]
                elif a[i-1].upper() == b[j-1]:
                    cache[i][j] = cache[i-1][j-1] or cache[i-1][j]
                elif a[i-1].islower():
                    cache[i][j] = cache[i-1][j]

    return "YES" if cache[al][bl] else "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
