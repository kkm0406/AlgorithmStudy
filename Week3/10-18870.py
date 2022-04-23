import sys
n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
newList = sorted(list(set(arr)))
dic = {newList[i]: i for i in range(len(newList))} #딕셔너리 시간 복잡도: O(1)
for i in arr:
    print(dic[i], end=' ')


#딕셔너리를 이용





