# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin, stdout
inS, outS = [], []
q = int(stdin.readline().strip())
for _ in range(q):
    line = stdin.readline().split()
    if line[0] == "1":
        inS.append(line[1])
    elif line[0] == "2":
        if not outS:
            while inS:
                outS.append(inS.pop())
        outS.pop()
    elif line[0] == "3":
        if outS:
            stdout.write(outS[-1]+"\n")
        else:
            stdout.write(inS[0]+"\n")