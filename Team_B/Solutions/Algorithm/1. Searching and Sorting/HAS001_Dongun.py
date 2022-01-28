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
    # Write your code here
    min = sys.maxsize
    price = sorted(((v, i) for i, v in enumerate(price)), reverse=True)
    for i in range(len(price)-1):
        if price[i][0]-price[i+1][0] < min and price[i][1]<price[i+1][1]:
            min = price[i][0]-price[i+1][0]
    return min
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
