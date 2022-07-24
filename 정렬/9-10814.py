import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = input().split()
    arr.append((int(a), i, b))

arr.sort()
for i in range(len(arr)):
    print(arr[i][0], arr[i][2])
