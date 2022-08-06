import sys

n = int(sys.stdin.readline())
dp = [0]*11
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(n):
    num = int(sys.stdin.readline())
    for i in range(4, num+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[num])