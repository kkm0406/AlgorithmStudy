import sys

tmp = sys.stdin.readline().strip()
tmp = tmp.upper()
cnt = {}
a = ""
for i in tmp:
    if i not in a:
        cnt[i] = tmp.count(i)
        a += i

newCnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

if len(newCnt) == 1:
    print(newCnt[0][0])
else:
    if newCnt[0][1] == newCnt[1][1]:
        print('?')
    else:
        print(newCnt[0][0])
