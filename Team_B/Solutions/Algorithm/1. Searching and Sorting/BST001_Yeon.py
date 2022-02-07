n = int(input())
m = list(map(int, input().split()))
d=sorted(m)
result = {}
result[d[0]] = 0
j = 1
for i in range(1,n):
    if d[i] == d[i-1]:
        continue
    else:
        result[d[i]] = j
        j+=1
        
for k in m:
    print(result[k],end=' ')
