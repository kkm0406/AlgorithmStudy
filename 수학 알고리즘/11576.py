import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.reverse()

tmp = 0
for i in range(m):
    tmp += num[i] * (a ** i)

ret = []

while tmp // b:
    ret.append(tmp % b)
    tmp //= b

ret.append(tmp)
ret.reverse()
print(' '.join(map(str, ret)))

