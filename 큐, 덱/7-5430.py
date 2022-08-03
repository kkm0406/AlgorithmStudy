import sys
import re
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].split(',')
    queue = deque(arr)
    if n == 0:
        queue = []
    cnt = 0
    flag = 0
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(queue) == 0:
                flag = 1
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if cnt % 2 == 0:
            print('[' + ",".join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ",".join(queue) + ']')
