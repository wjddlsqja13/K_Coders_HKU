n = input()
x = [int(x) for x in input().split()]
sort = sorted(x)
new = {}
output = 0


for k in range(len(sort)) :
    new[sort[k]] = output
    if k == len(sort)-1 :
        break
    if sort[k]!=sort[k+1] :
        output += 1

for i in range(len(x)) : 
     x[i] = new[x[i]]

for num in x:
    print(num,end=" ")