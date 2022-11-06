import sys
n, k = map(int, sys.stdin.readline().split())
list = []
cnt = 0
for i in range(1, n):
    if n%i==0:
        cnt += 1
        if cnt == k:
            print(i)
            exit(0)

print(0)
