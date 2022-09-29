import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
left, right = 0, 1

while left <= right <= n:
    tmp = a[left:right]
    tmpSum = sum(tmp)

    if tmpSum == m:
        cnt += 1
        right += 1
    elif tmpSum < m:
        right += 1
    else:
        left += 1

print(cnt)
