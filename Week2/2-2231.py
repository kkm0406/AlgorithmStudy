n = int(input())
sum = 0
for i in range(1, n + 1):
    tmpSum = 0
    for j in str(i):
        tmpSum += int(j)
    if tmpSum+i == n:
        sum = tmpSum+i
        break
print(sum)
