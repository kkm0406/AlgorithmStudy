n = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append((len(a), a))

arr = set(arr)

newArr = list(arr)
newArr.sort()

for i in range(len(newArr)):
    print(newArr[i][1])

