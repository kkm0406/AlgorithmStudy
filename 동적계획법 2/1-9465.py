import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp2 = list(map(int, sys.stdin.readline().split()))
    arr = [tmp, tmp2]
    for i in range(1, n):
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    print(max(arr[0][n-1], arr[1][n-1]))