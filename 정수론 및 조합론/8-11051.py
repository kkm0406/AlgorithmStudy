import sys

n, k = map(int, sys.stdin.readline().split())
dp = []

for i in range(n + 1):
    dp.append([1] * (i + 1))

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j])

print(dp[n][k] % 10007)
