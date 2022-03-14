# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin, maxsize
import heapq

t = int(input())

for _ in range(t):
    l = [int(i) for i in stdin.readline().split()]
    n, x = l[0], l[1:]
    
    if n == 0:
        print(0)
        continue
    
    x.sort()
    
    teams = {}
    for i in range(n):
        if x[i]-1 in teams and len(teams[x[i]-1]):
            l = heapq.heappop(teams[x[i]-1])
            if x[i] in teams:
                heapq.heappush(teams[x[i]], l+1)
            else:
                teams[x[i]] = [l+1]
        else:
            if x[i] in teams:
                heapq.heappush(teams[x[i]], 1)
            else:
                teams[x[i]] = [1]
    
    ans = maxsize
    
    for _, v in teams.items():
        if v:
            for l in v:
                ans = min(ans, l)
                
    print(ans)