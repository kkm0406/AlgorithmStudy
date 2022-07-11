import sys

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

dp = [[0] * (k + 1) for _ in range(n + 1)]
wv = [[0, 0]]
for _ in range(n):
    wv.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = wv[i][0]
        v = wv[i][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])

# dp[n][k]는 n번째 물건까지 살펴보았을 떄, 무게가 k인 배낭의 최대 가치
# 물건을 배낭에 담을 떄
# 1. 현재 배낭의 허용 무게보다 넣을 무건의 무게가 더 크다면 넣지 않는다.
# 2. 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다.
# 2-1. 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
# 2-2. 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
# ① j < weight : d[i][j] = d[i-1][j]
# ② d[i][j] = max( d[i-1][ j-weight ]+value ), d[i-1][j] )
