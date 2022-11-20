import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
a = 0
b = 0
c = 0


def divide(n, arr):
    global a
    global b
    global c
    check1 = 0
    check2 = 0
    check3 = 0
    for i in range(n):
        check1 += arr[i].count(-1)
        check2 += arr[i].count(0)
        check3 += arr[i].count(1)
    if check1 != 0 and check2 == 0 and check3 == 0:
        a += 1
    elif check2 != 0 and check1 == 0 and check3 == 0:
        b += 1
    elif check3 != 0 and check2 == 0 and check1 == 0:
        c += 1
    else:
        tmp = [arr[i][0:n // 3] for i in range(0, n // 3)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3: n // 3 * 2] for i in range(0, n // 3)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3 * 2: n] for i in range(0, n // 3)]
        divide(n // 3, tmp)
        tmp = [arr[i][0:n // 3] for i in range(n // 3, n // 3 * 2)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3: n // 3 * 2] for i in range(n // 3, n // 3 * 2)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3 * 2: n] for i in range(n // 3, n // 3 * 2)]
        divide(n // 3, tmp)
        tmp = [arr[i][0:n // 3] for i in range(n // 3 * 2, n)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3: n // 3 * 2] for i in range(n // 3 * 2, n)]
        divide(n // 3, tmp)
        tmp = [arr[i][n // 3 * 2: n] for i in range(n // 3 * 2, n)]
        divide(n // 3, tmp)


divide(n, arr)
print(a)
print(b)
print(c)
