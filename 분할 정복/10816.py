import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
arr.sort()
left = 0
right = n - 1

cnt = {}
for i in arr:
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] = 1


def binarySearch(i, left, right):
    while left <= right:
        mid = (left + right) // 2
        if i == arr[mid]:
            print(cnt.get(i), end=" ")
            return 1
        elif arr[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    print(0, end=" ")
    return 0


for i in card:
    binarySearch(i, left, right)

