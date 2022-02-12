#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    a_sorted = [a[0]]
    median_list = [a[0]]
    
    for i in range(1,len(a)) :
        bisect.insort(a_sorted,a[i])
        length = len(a_sorted)
        if (length % 2 == 0) :
            med_index = int(length / 2)
            median = (a_sorted[med_index-1] + a_sorted[med_index]) / 2
        else :
            median = a_sorted[length//2]
        median_list.append(round(median,1))
    
    return median_list
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
