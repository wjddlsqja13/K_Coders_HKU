from sys import stdin,stdout

n = int(stdin.readline().rstrip())
stack1 = []
stack2 = []
for i in range(n):
    data = stdin.readline().rstrip().split()
    if data[0] == '1':
        if not stack1:
            first = data[1]
        stack1.append(data[1])
    elif data[0] == '2':
        if not stack2:
            while stack1:
                stack2.append(stack1.pop())
        stack2.pop()
    elif data[0] == '3':
        if stack2:
            stdout.write(stack2[-1]+"\n")
        else:
            stdout.write(first+"\n")   
