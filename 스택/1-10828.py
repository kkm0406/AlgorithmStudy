import sys

n = int(sys.stdin.readline())
stack = []

while n:
    operation = sys.stdin.readline().split()
    if operation[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif operation[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif operation[0] == 'size':
        print(len(stack))
    elif operation[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        stack.append(operation[1])
    n -= 1
