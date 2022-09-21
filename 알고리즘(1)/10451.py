import sys

t = int(sys.stdin.readline())


def dfs(i):
    flag[i] = 1
    next = arr[i]
    if flag[next] == 0:
        dfs(next)


while t:
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = [0] + arr
    flag = [0] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if flag[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)
    t -= 1
