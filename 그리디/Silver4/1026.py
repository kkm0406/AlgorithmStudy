import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
brr = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
result = 0
for i in range(n):
    result += arr[i] * brr[i]
print(result)
