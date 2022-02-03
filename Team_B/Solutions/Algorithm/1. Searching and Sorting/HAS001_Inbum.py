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
    s = sorted(enumerate(price),key=lambda kv:kv[1])
    return min((s[i+1][1]-s[i][1] for i in range(len(s)-1) if s[i+1][0]<s[i][0]))