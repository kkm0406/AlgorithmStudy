from itertools import permutations #순열을 구하는 내장함수
import sys

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(i + 1)
for i in permutations(nums, m):
    print(*i)
