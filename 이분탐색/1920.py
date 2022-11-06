import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()


def binary_search(i):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] < i:
            start = mid + 1
        elif a[mid] > i:
            end = mid - 1
        else:
            return 1

    return 0


for i in b:
    print(binary_search(i))
