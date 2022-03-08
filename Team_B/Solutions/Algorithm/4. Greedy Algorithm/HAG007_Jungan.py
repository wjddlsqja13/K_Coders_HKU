#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cost = 0
    c.sort(reverse=True)
    cost += sum(c[:k])
    remaining = c[k:]
    count, factor = 1 , 2
    
    for i in remaining : 
        cost += i * factor
        if count < k : 
            count += 1
        else : 
            count = 1
            factor += 1
    
    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
