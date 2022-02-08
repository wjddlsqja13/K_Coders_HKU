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
    # Write your code here
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        else:
            if not stack:
                return "NO"
            top = stack[-1]
            if top == "(" and c == ")" or top == "{" and c == "}" or top == "[" and c == "]":
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
