from sys import stdin

N = int(input())
ls = [list(map(str, stdin.readline().split())) for _ in range(N)]  # input() 대신 stdin.readline()을 쓰면 훨씬 빠름
ans = sorted(ls, key=lambda x: int(x[0]))
for a in ans:
    print(a[0], a[1])
