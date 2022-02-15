#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

#Time limit exceeded
def poisonousPlants(p):
    # Write your code here
    ss = []
    idx = 1
    s = [p[idx-1]]
    
    while idx < len(p):
        if p[idx] > p[idx-1]:
            ss.append(s)
            s = [p[idx]]
        else:
            s.append(p[idx])
        idx += 1
    ss.append(s)
    
    ans = 0
    
    while len(ss) > 1: 
        #print(ss)  
        i = 1    
        while i < len(ss):
            if ss[i-1][-1] < ss[i][0]:
                ss[i] = ss[i][1:]
                if len(ss[i]) == 0:
                    ss = ss[:i] + ss[i+1:]
                    continue
                elif ss[i-1][-1] >= ss[i][0]:
                    ss[i-1] = ss[i-1] + ss[i]
                    ss = ss[:i] + ss[i+1:]
                    continue
            i += 1
        ans += 1
        #print(ss)
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
