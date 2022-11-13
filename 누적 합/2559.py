import sys

n, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0]

for i in range(len(arr)):
    dp.append(arr[i]+dp[i])


result = []
for i in range(k, len(dp)):
    result.append(dp[i] - dp[i-k])

print(max(result))