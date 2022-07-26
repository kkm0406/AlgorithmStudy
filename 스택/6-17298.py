import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ret = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        ret[stack.pop()] = arr[i]
    stack.append(i)

print(*ret)
