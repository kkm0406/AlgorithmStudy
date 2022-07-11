import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0]

for i in range(len(arr)):
    dp.append(arr[i]+dp[i])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b]-dp[a-1])
