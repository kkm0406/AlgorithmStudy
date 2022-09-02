import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

white = 0
blue = 0


def divide(n, arr):
    global white
    global blue
    check = 0
    for i in range(n):
        check += sum(arr[i])
    if check == 0:
        white += 1
    elif check == n ** 2:
        blue += 1
    else:
        tmp = [arr[i][0:n // 2] for i in range(0, n // 2)]
        divide(n // 2, tmp)
        tmp = [arr[i][0:n // 2] for i in range(n // 2, n)]
        divide(n // 2, tmp)
        tmp = [arr[i][n // 2:n] for i in range(0, n // 2)]
        divide(n // 2, tmp)
        tmp = [arr[i][n // 2:n] for i in range(n // 2, n)]
        divide(n // 2, tmp)


divide(n, arr)

print(white)
print(blue)
