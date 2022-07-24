import sys
from collections import defaultdict

m = int(sys.stdin.readline())

for i in range(m):
    n = int(sys.stdin.readline())
    clothes = defaultdict(list) #디폴트값이 list인 딕셔너리
    arr = []
    for j in range(n):
        a, b = map(str, sys.stdin.readline().split())
        clothes[b].append(a) #리스트 형식에 동적으로 push
        arr.append(b) #입력한 옷의 종류 push
    arr = list(set(arr)) #옷의 종류 수를 위해 집합화한 후 list화
    clothes = dict(clothes) #일반적인 딕셔너리로 
    num = 1
    for k in range(len(arr)):
        num *= len(clothes[arr[k]])+1 #의상을 입거나 안입거나
    print(num-1) #모든 의상을 안입을 경우를 제외

