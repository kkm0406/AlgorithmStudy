import sys

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        q.append(op[1])
    elif op[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif op[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif op[0] == "size":
        print(len(q))
    elif op[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            del q[0]
