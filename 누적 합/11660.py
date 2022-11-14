import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
result = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        result[i+1][j+1] = arr[i][j] + result[i][j + 1] + result[i + 1][j] - result[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(result[x2][y2] + result[x1-1][y1-1] - result[x1-1][y2] - result[x2][y1-1])
