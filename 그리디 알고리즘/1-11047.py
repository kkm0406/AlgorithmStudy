import sys

n, k = map(int, sys.stdin.readline().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

arr.reverse()
cnt = 0
for i in arr:
    if k >= i:
        tmp = k // i
        k -= i * tmp
        cnt += tmp
    if k == 0:
        break

print(cnt)
