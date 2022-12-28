import sys

while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break
    num = "".join(reversed(n))
    if num == n:
        print('yes')
    else:
        print('no')