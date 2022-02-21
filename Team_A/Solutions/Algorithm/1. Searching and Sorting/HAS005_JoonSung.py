#HAS005

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    pointer = arr[-1]
    i = n-1
    while i > 0 and arr[i-1] > pointer :
        arr[i] = arr[i-1]
        i -= 1
        print(*arr)
    arr[i] = pointer
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
