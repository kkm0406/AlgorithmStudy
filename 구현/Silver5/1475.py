import sys

N = sys.stdin.readline().strip()
N = N.replace('9', '6')
nums = [0] * 10

for i in N:
    nums[int(i)] += 1

if nums[6] % 2 == 0:
    nums[6] = nums[6] // 2
else:
    nums[6] = nums[6] // 2 + 1

print(max(nums))
