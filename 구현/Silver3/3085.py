import sys

N = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = 1


def count():
    global result
    for i in range(N):
        tmp = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j + 1]:
                tmp += 1
            else:
                tmp = 1
            if tmp > result:
                result = tmp

        tmp = 1
        for j in range(N-1):
            if arr[j][i] == arr[j + 1][i]:
                tmp += 1
            else:
                tmp = 1
            if tmp > result:
                result = tmp


for i in range(N):
    for j in range(N):
        if i + 1 < N:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            count()
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
        if j + 1 < N:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            count()
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

print(result)
