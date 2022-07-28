import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque()
ans = []
for i in range(1, n + 1):
    q.append(i)

while len(q) > 0:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print('<', end="")
for i in range(len(ans)-1):
    print(f"{ans[i]}, ", end="")
print(ans[-1], end="")
print('>', end="")

