from sys import stdin

N = int(input())
ls = [stdin.readline().strip() for _ in range(N)] # strip()으로 개행문자 제거
ls = list(dict.fromkeys(ls))
ans = sorted(ls, key=lambda x: (len(x), x))
for a in ans:
    print(a)
