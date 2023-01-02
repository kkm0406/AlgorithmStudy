import sys

S = int(sys.stdin.readline())
result = 0
cnt = 0

while True:
    cnt += 1
    result += cnt
    if result > S:
        print(cnt - 1)
        break
