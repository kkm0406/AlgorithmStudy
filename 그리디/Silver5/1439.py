import sys

S = sys.stdin.readline().strip()

if S.count('0') < S.count('1'):
    flip = '0'
else:
    flip = '1'

cnt = 0

if S[0] == flip:
    for i in range(1, len(S)):
        if S[i - 1] == flip and S[i] != flip:
            cnt += 1
else:
    for i in range(1, len(S)):
        if S[i - 1] != flip and S[i] == flip:
            cnt += 1


print(cnt)