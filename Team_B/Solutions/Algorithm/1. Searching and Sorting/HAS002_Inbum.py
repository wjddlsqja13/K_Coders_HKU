#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    prefix = 0
    maxim = 0
  
    S = set()  
    S.add(0)      
    n = len(a)
    
    for i in range(n):  
  
        # Finding prefix sum.  
        prefix = (prefix + a[i]) % m  
  
        # Finding maximum of prefix sum.  
        maxim = max(maxim, prefix)  
  
        # Finding iterator pointing to the first  
        # element that is not less than value  
        # "prefix + 1", i.e., greater than or  
        # equal to this value. 
        it = 0
        for i in S: 
            if i >= prefix + 1: 
                it = i 
        if (it != 0) : 
                maxim = max(maxim, prefix - it + m )  
  
        # adding prefix in the set.  
        S.add(prefix)  
  
    return maxim 