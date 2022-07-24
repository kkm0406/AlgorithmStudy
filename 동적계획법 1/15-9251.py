txt1 = input()
txt2 = input()
dp = [[0] * (len(txt2) + 1) for _ in range(len(txt1) + 1)]

for i in range(1, len(txt1) + 1):
    for j in range(1, len(txt2) + 1):
        if txt1[i - 1] == txt2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
