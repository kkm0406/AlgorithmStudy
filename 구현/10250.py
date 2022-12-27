import math
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    room = math.ceil(n / h)
    if n % h == 0:
        floor = h
        print(f'{floor*100+room}')
    else:
        floor = n % h
        print(f'{floor*100+room}')
