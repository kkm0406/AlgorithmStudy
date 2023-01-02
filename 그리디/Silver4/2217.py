import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr = sorted(arr)
brr = sorted(arr, reverse=True)
result = 0

for i in range(len(arr)):
    result = max(result, max(brr[i], arr[i]*(N-i)))

print(result)



