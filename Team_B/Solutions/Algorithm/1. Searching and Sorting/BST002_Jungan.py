n = int(input()) 
age = [0 for _ in range(n)]
name = [0 for _ in range(n)]
output = []
for i in range(n) :
    age[i],name[i] = input().split()
    
for j in range(n) :
    output.append([int(age[j]),name[j],j])

sort = sorted(output,key=lambda x:(x[0],x[2]))

for k in range(n) :
    print(str(sort[k][0])+" "+sort[k][1])