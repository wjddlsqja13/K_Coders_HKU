#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    count = 0
    sort = sorted(expenditure[:d])
    for i in range(d,len(expenditure)-1) :
        #d가 짝수일 경우
        if d % 2 == 0 : 
            median = (sort[d//2-1] + sort[d//2] ) /2
        else : #d가 홀수일 경우
            median = sort[d//2]
        
        if expenditure[i] >= 2 * median :
            count +=1
        
        #for문을 반복할때마다 정렬을 다시 했더니 timeout이 발생, bisect을 사용하면 정렬을 다시 할 필요가 없음
        #가장 앞에 있는 원소를 delete
        del sort[bisect.bisect_left(sort,expenditure[i-d])]
        #새로운 원소를 추가 + 정렬
        bisect.insort(sort,expenditure[i])
        
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
