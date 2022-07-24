import sys

n = int(sys.stdin.readline())

for k in range(n):
    a, b = map(int, sys.stdin.readline().split())
    dp = []
    for i in range(b + 1):
        dp.append([1] * (i + 1))
    for i in range(2, b + 1):
        for j in range(1, i):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j])
    print(dp[b][a])
