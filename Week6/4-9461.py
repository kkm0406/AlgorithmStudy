import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    dp = [1] * num
    for i in range(3, num):
        dp[i] = dp[i - 3] + dp[i - 2]
    print(dp[-1])
