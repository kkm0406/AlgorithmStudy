import sys

a, p = map(int, sys.stdin.readline().split())
arr = [a]

while True:
    num = 0
    for i in str(arr[-1]):
        num += int(i) ** p
    if num in arr:
        print(arr.index(num))
        break
    arr.append(num)

