#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    q = deque([[startX, startY, 0]])
    visited = [[False] * len(grid) for _ in range(len(grid))]
    visited[startX][startY] = True
    ans = sys.maxsize
    move = 0
    print(grid)
    while q:
        cur = q.popleft()
        if cur[0] == goalX and cur[1] == goalY:
            ans = min(ans, cur[2])
        x = 1
        while cur[0] - x >= 0 and grid[cur[0]-x][cur[1]] != 'X':
            if not visited[cur[0]-x][cur[1]]:
                q.append([cur[0]-x, cur[1], cur[2]+1])
                visited[cur[0]-x][cur[1]] = True
            x += 1
        x = 1
        while cur[0] + x < len(grid) and grid[cur[0]+x][cur[1]] != 'X':
            if not visited[cur[0]+x][cur[1]]:
                q.append([cur[0]+x, cur[1], cur[2]+1])
                visited[cur[0]+x][cur[1]] = True
            x += 1
        y = 1
        while cur[1] - y >= 0 and grid[cur[0]][cur[1]-y] != 'X':
            if not visited[cur[0]][cur[1]-y]:
                q.append([cur[0], cur[1]-y, cur[2]+1])
                visited[cur[0]][cur[1]-y] = True
            y += 1
        y = 1
        while cur[1] + y < len(grid) and grid[cur[0]][cur[1]+y] != 'X':
            if not visited[cur[0]][cur[1]+y]:
                q.append([cur[0], cur[1]+y, cur[2]+1])
                visited[cur[0]][cur[1]+y] = True
            y += 1
        move += 1
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
