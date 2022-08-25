import sys

n = sys.stdin.readline().rstrip()
arr = []
for i in range(0, len(n)):
    arr.append(n[i:])

arr.sort()

for i in arr:
    print(i)
