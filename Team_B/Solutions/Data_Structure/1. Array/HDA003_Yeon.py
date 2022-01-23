import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    #Brute Force 방법을 쓰면 시간 초과됨, 그래서 prefix sum 알고리즘 사용
    result = [0] * (n+2)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        result[a] += k
        result[b+1] -= k
    #출력할때도 아래처럼 모든값들을 계산하려면 시간이 초과됨, 최댓값만 필요하기 때문에 굳이 전부 계산 안하고 비교 연산만 해주는게 시간 단축에 용이
    '''
    answer = [0] 
    for i in range(1,len(result)):
        answer.append(result[i]+answer[i-1])
    return max(answer)
    '''
    max_value = 0
    prefix_sum = 0
    for i in result:
        prefix_sum += i
        if prefix_sum > max_value:
            max_value = prefix_sum
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
