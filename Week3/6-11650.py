n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])
