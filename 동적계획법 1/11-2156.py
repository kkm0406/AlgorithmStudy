n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])

# w3 = w1+w2, w1+w3, w2+w3
# 첫번째 경우는 이전 dp값
# 두번째 경우는 i-3dp값+w[i-1]+w[i]
# 세번째 경우는 i-2dp값+w[i]