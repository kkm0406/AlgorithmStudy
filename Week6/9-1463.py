import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])

# 9의 경우 9->3->1
# 3의 경우 3->1
# -> 앞에서 구한 결과값으 저장하였다가 후에 사용
