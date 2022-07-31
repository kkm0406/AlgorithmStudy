import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, n + 1)])
cnt = 0
for i in arr:
    while i != deq[0]:
        if deq.index(i) <= len(deq) / 2:
            tmp = deq.popleft()
            deq.append(tmp)
            cnt += 1
        else:
            tmp = deq.pop()
            deq.appendleft(tmp)
            cnt += 1
    deq.popleft()


print(cnt)
