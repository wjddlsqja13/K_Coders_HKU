#!/bin/python3
# Pypy3으로 통과
import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    # Write your code here
    count = 0
    mod = 10**9+7
    c3 = [[0] * 26 for _ in range(26)]
    c2 = [[0] * 26 for _ in range(26)]
    c1 = [0] * 26
    for c in s:
        v = ord(c) - ord('a')
        for i in range(26):
            count = (count + c3[v][i]) % mod                  # vxxv
            c3[i][v] = (c3[i][v] + c2[i][v]) % mod            # xvv
            c2[i][v] = (c2[i][v] + c1[i]) % mod               # xv
        c1[v] += 1                                            # v
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
