from sys import stdin

N = int(input())
X = [int(i) for i in stdin.readline().split()]

sortedX = sorted(((v, i) for i, v in enumerate(X)))

v = 0
X[sortedX[0][1]] = 0

for i in range(1, N):
    if sortedX[i][0] > sortedX[i-1][0]:
        v += 1
    X[sortedX[i][1]] = v

for n in X:
    print(n, end=' ')
