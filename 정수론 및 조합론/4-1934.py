import sys

n = int(sys.stdin.readline())


def find(n1, n2):
    if n2 == 0:
        return n1
    else:
        return find(n2, n1 % n2)


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    n1 = max(a, b)
    n2 = min(a, b)
    print(int(n1 * n2 / find(n1, n2)))
