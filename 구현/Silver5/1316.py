import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    arr = ""
    idx = -1
    flag = True
    for i in word:
        if i not in arr or arr[-1] != i:
            arr += i
    for i in arr:
        if arr.count(i) > 1:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)
