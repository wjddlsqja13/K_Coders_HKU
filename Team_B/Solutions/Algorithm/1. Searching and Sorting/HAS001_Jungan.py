#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    min = 1000000000000000000
    new_sorted = sorted(price)
    for i in range(len(new_sorted)-1) :
        if (new_sorted[i+1] - new_sorted[i]) < min and (price.index(new_sorted[i+1]) < price.index(new_sorted[i])) :
                min = new_sorted[i+1] - new_sorted[i]
            
    return min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()