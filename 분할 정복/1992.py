import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def divide(n, arr):
    check = 0
    for i in range(n):
        check += sum(arr[i])
    if check == 0:
        print(0, end='')
    elif check == n**2:
        print(1, end='')
    else:
        print('(', end='')
        tmp = [arr[i][0:n // 2] for i in range(0, n // 2)]
        divide(n // 2, tmp)
        tmp = [arr[i][n // 2: n] for i in range(0, n // 2)]
        divide(n // 2, tmp)
        tmp = [arr[i][0:n // 2] for i in range(n // 2, n)]
        divide(n // 2, tmp)
        tmp = [arr[i][n // 2: n] for i in range(n // 2, n)]
        divide(n // 2, tmp)
        print(')', end='')


divide(n, arr)

