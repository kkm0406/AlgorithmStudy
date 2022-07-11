import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간 기준으로 정렬
# 람다 key에 여러 함수면 해당 인자 순서대로 정렬

end = 0
cnt = 0
for i in range(n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)
