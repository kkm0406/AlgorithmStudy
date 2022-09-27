import sys

n = int(sys.stdin.readline())
people = {}
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        people[a] = 1
    else:
        people[a] -= 1

arr = []
for key in people:
    if not people[key] == 0:
        arr.append(key)

arr.sort()

for i in reversed(range(len(arr))):
    print(arr[i])
