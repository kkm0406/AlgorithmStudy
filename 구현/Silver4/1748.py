import sys

N = int(sys.stdin.readline())

lenN = len(str(N))

cnt = 0

for i in range(lenN - 1):
    cnt += 9 * (10 ** i) * (i + 1)

print(cnt + (N - 10 ** (lenN - 1) + 1) * lenN)
