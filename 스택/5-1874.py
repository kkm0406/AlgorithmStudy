import sys

n = int(sys.stdin.readline())
op = []
stack = []
num = 0
flag = True

for _ in range(n):
    x = int(input())

    while num < x:
        num += 1
        stack.append(num)
        op.append('+')

    if stack[-1] == x:
        stack.pop()
        op.append('-')
    else:
        flag = False
        break

if not flag:
    print('NO')
else:
    print('\n'.join(op))
