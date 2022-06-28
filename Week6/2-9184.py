import sys

dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


while True:
    a1, b1, c1 = map(int, sys.stdin.readline().split())
    if a1 == -1 and b1 == -1 and c1 == -1:
        break
    print(f"w({a1}, {b1}, {c1}) = {w(a1, b1, c1)}")
