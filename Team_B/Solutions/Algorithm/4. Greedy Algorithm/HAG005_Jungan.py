#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    sorted_arr = sorted(arr,reverse = True)
    arr_dict = {}
    
    for index, item in enumerate(arr) :
        arr_dict[item] = index
    
    for index, item in enumerate(sorted_arr) :
        if arr[index] != item :
            temp = arr[index]
            arr[index] = item
            arr[arr_dict[item]] = temp
            k -= 1
            if k == 0:
                return arr
            arr_dict[temp] = arr_dict[item]
            arr_dict[item] = index
    return arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
