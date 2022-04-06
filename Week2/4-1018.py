n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

cnt = []
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'W':
                        cnt1 += 1
                    if arr[a][b] != 'B':
                        cnt2 += 1
                else:
                    if arr[a][b] != 'B':
                        cnt1 += 1
                    if arr[a][b] != 'W':
                        cnt2 += 1
        cnt.append(cnt1)
        cnt.append(cnt2)


print(min(cnt))
