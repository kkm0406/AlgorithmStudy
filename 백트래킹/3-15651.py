import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(i + 1)

for i in product(nums, repeat=m): #결과: 중첩된 for loop에 해당하는 데카르트의 곱
    print(*i)
