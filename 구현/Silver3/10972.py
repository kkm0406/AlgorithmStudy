import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        for j in range(N - 1, 0, -1):
            if arr[i - 1] < arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[i - 1]
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()

print(-1)
