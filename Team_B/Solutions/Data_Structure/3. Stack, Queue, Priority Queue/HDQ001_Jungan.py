# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
from collections import deque

q = sys.stdin.readline()

queue = deque([])

for i in range(int(q)) :
    x = sys.stdin.readline().split()
    if int(x[0]) == 1: 
        queue.append(x[1])
    elif int(x[0]) == 2:
        queue.popleft()
    else :
        sys.stdout.write(queue[0]+"\n")
        