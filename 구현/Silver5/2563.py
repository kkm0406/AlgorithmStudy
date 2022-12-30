import sys

n = int(sys.stdin.readline())
arr = [[0]*100 for _ in range(100)]
result = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

for i in arr:
    result += i.count(1)

print(result)