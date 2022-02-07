#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    dic = {'}' : '{', ']' : '[', ')' : '('}
    stack = []
    for i in s :
        if stack and i in dic and dic[i] == stack[-1]: 
            stack.pop()
        else:
            stack.append(i)
        
    if stack :
        return "NO"
    else :
        return "YES"    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
