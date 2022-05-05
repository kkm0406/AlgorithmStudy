import sys

n = int(sys.stdin.readline())

num = 1
for i in range(1, n + 1):
    num *= i

num = str(num)
cnt = 0

for i in reversed(range(len(num))):
    if num[i] == '0':
        cnt += 1
    else:
        break

print(cnt)