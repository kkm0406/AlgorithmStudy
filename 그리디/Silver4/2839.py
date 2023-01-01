import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n // 5, -1, -1):
    tmp_num = n - (i * 5)
    cnt = i
    if tmp_num % 3 == 0:
        arr.append(cnt + tmp_num // 3)

if len(arr) == 0:
    print(-1)
else:
    print(min(arr))
