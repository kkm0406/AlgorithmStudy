import sys

k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
w = 0
h = 0
idx_w = 0
idx_h = 0
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            idx_w = i
    else:
        if h < arr[i][1]:
            h = arr[i][1]
            idx_h = i

tmp_width = abs(arr[(idx_w - 1) % 6][1] - arr[(idx_w + 1) % 6][1])
tmp_height = abs(arr[(idx_h - 1) % 6][1] - arr[(idx_h + 1) % 6][1])
print(((w * h) - (tmp_height * tmp_width)) * k)
