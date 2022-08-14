import sys
from collections import deque

n = int(sys.stdin.readline())
listA = (list(map(int, sys.stdin.readline().split())))
listB = (list(map(int, sys.stdin.readline().split())))

newA = []
newB = []

initIdx = listB.index(listA[0])

start = initIdx - n
end = initIdx
for i in range(start, end):
    newA.append(listB[i])

start = initIdx
end = initIdx - n

for i in range(start, end, -1):
    newB.append(listB[i])

if newA == listA or newB == listA:
    print('good puzzle')
else:
    print('bad puzzle')

