import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]
arr = deque(arr)
brr = []
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    brr.append(arr.popleft())

print('<', end='')
for i in range(n-1):
    print(f'{brr[i]}, ', end='')
print(f'{brr[-1]}>')
