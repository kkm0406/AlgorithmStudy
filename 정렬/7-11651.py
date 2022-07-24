import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((b, a))

arr.sort() #sort할 때 첫번째 요소가 같으면 두번째 요소 비교
for i in range(len(arr)):
    print(arr[i][1], arr[i][0])



