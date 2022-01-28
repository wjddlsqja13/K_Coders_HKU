#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    # Write your code here
    sortedTrack = sorted(track,key=lambda x: (x[0], x[1]))
    ans = m * n
    tracks = []
    for i in range(len(sortedTrack)):
        if len(tracks) == 0 or sortedTrack[i][0] != tracks[0][0]:
            tracks.insert(0, [sortedTrack[i][0], sortedTrack[i][1], sortedTrack[i][2]])
        else:
            if sortedTrack[i][1] >= tracks[0][1]: 
                if sortedTrack[i][1] <= tracks[0][2]:
                    if sortedTrack[i][2] > tracks[0][2]:
                        tracks[0][2] = sortedTrack[i][2]
                else:
                    tracks.insert(0, [sortedTrack[i][0], sortedTrack[i][1], sortedTrack[i][2]])
                
            
    for t in tracks:
        ans -= t[2] - t[1] + 1                            
                    
    return ans
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
