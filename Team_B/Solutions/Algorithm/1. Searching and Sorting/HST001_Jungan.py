#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):

    new = sorted(arr)
    min = 999999999999
    output = []
    for i in range(len(new)-1) :
        for j in range(i+1,len(new)):
            if new[j] - new[i] < min :
                #가장 작은 difference 찾기
                min = new[j] - new[i]
    
    for i in range(len(new)-1) :
        for j in range(i+1,len(new)):
            #min을 difference로 갖고 있는 모든 짝을 찾기
            if new[j] - new[i] == min :
                output.append(new[i])
                output.append(new[j])
    
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
