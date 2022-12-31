import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()
arr = []
for i in range(1, N + 1):
    deq.append(i)

while len(deq) > 1:
    drop = deq[0]
    deq.popleft()
    arr.append(drop)
    move = deq[0]
    deq.append(move)
    deq.popleft()

for i in arr:
    print(i, end=' ')
print(deq[0])
