n = int(input())
arr = []
for i in range(n):
    arr.append((int(input())))
num = 0
for i in range(0, len(arr)-1):
    num = i
    for j in range(i + 1, len(arr)):
        print(num, arr[j])
        if arr[j] < arr[num]:
            arr[num], arr[j] = arr[j], arr[num]

for i in arr:
    print(i)