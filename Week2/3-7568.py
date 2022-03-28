n = int(input())
arr = []
order = []
for i in range(0, n):
    arr.append(list(map(int, input().split())))
for i in range(0, len(arr)):
    cnt = 1
    for j in range(0, len(arr)):
        if arr[i] != arr[j]:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    order.append(cnt)

for i in range(len(order)):
    print(order[i], end=' ')

