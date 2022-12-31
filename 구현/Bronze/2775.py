import sys

t = int(sys.stdin.readline())
floor = [[0 for i in range(16)] for j in range(15)]

for i in range(1, 15):
    floor[0][i] = i

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    if k == 0:
        print(n)
    else:
        for i in range(1, k+1):
            for j in range(1, n+1):
                floor[i][j] = floor[i][j-1] + floor[i-1][j]
        print(floor[k][n])



