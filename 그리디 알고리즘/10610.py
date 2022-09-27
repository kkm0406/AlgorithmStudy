import sys

n = sys.stdin.readline().rstrip()

n = sorted(n, reverse=True)

if '0' not in n:
    print(-1)
else:
    result = 0
    for i in n:
        result += int(i)
    if not result % 3 == 0:
        print(-1)
    else:
        print(''.join(n))
