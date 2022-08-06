import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = [0] + arr
dp = [0]*(n+1)
dp[1] = arr[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+arr[j])

print(dp[-1])