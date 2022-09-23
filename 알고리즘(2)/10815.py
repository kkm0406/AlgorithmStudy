import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

nums.sort()
left = 0
right = len(nums) - 1


def search(target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


for i in cards:
    print(search(i, 0, right), end=" ")
