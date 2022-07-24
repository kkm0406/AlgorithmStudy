from itertools import combinations #조합을 구하는 내장함수
import sys

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(i + 1)
for i in list(combinations(nums, m)):
    print(*i)
