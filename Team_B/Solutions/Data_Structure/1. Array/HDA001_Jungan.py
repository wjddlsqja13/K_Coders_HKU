#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # max가 작은 숫자일수 있으니 최대한 작은 값으로 설정
    max = -9999999;
    #array는 항상 6x6이고 hourglass의 가로와 세로 길이가 각각 3이니 가로,세로를 4번씩 loop
    for i in range(4) :
        for j in range(4):
            sum = 0;
            for k in range(i,i+3) :
                if k==i or k==i+2 :
                    sum += arr[k][j]+arr[k][j+1]+arr[k][j+2];
                elif k == i+1:
                    sum += arr[k][j+1];
            if sum > max :
                max = sum;
    
    return max ;
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()