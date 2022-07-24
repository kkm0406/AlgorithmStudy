import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(i + 1)

for i in combinations_with_replacement(nums, m):
    print(*i)
