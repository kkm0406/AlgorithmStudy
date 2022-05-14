import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
result = []


def cal(ret, idx):
    if idx == n:
        result.append(ret) #n번째 인덱스까지의 계산 결과를 push
    for i in range(4): #op의 개수만큼 for문 실행
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                cal(ret + num[idx], idx + 1) #DFS를 사용해 연산 실행
            elif i == 1:
                cal(ret - num[idx], idx + 1)
            elif i == 2:
                cal(ret * num[idx], idx + 1)
            elif i == 3:
                if ret < 0 and num[idx] > 0:
                    tmp = -ret // num[idx]
                    cal(-tmp, idx + 1)
                else:
                    cal(ret // num[idx], idx + 1)
            op[i] += 1 #백트래킹을 위해 원래 상태로 돌림


cal(num[0], 1) #첫번째 숫자에 첫번째 연산자 인덱스를 넣음

result.sort()

print(result[-1])
print(result[0])
