import sys

n, m = map(int, sys.stdin.readline().split())
name = {}
arr = []
num = n + m
while num:
    tmp = input()
    if name.get(tmp) == 1:
        arr.append(tmp)
    else:
        name[tmp] = 1
    num -= 1

arr.sort()
print(len(arr))
for i in arr:
    print(i)
