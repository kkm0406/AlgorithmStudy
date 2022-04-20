import statistics
from collections import Counter

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

ave = sum(arr) / n
mid = statistics.median(arr)
cnt = Counter(arr).most_common()

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        finalCnt = cnt[1][0]
    else:
        finalCnt = cnt[0][0]
else:
    finalCnt = cnt[0][0]

range = max(arr) - min(arr)

print(round(ave))
print(mid)
print(finalCnt)
print(range)
