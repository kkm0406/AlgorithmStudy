import sys

n, m, k = map(int, sys.stdin.readline().split())

cnt = 0
while True:
    n -= 2
    m -= 1
    if n < 0 or m < 0 or n + m < k:
        break
    else:
        cnt += 1

print(cnt)
