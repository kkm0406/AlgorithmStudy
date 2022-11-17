# lambda 매개변수 : 표현식
from functools import reduce

print((lambda x, y: x + y)(10, 30))

arr = list(map(lambda x: x ** 2, range(5)))
print(arr)

# reduce: 누적계산
arr1 = reduce(lambda x, y: y + x, 'abcde')
print(arr1)

# filter
arr2 = list(filter(lambda x: x % 2, [1, 4, 25, 234, 256, 55, 23, 56]))
print(arr2)

texts = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
for i in texts:
    if (lambda x: x == i[::-1])(i):
        print(i)

nums = [19, 65, 57, 39, 152, 693, 121, 44, 90, 190]
for i in nums:
    if (lambda x: not x % 13 or not x % 19)(i):
        print(i)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(list(map(lambda x: nums1[x]+nums2[x], range(3))))
