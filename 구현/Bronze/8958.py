import sys
n = int(sys.stdin.readline())
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    result = 0
    prev = ""
    cnt = 1
    for i in tmp:
        if prev == 'O' and i == 'O':
            cnt += 1
        elif prev != 'O' and i == 'O':
            cnt = 1
        else:
            cnt = 0
        result += cnt
        prev = i
    print(result)
