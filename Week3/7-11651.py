import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((b, a))

arr.sort()
for i in range(len(arr)):
    print(arr[i][1], arr[i][0])


