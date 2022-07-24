import sys

a, b = map(int, sys.stdin.readline().split())

numA = 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        numA = i

print(numA)

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

