import sys

n = int(sys.stdin.readline())
arr = [0] * 10001  # 리스트를 0으로 초기화

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] = arr[num] + 1
    # 입력값을 받을 때마다 입력값과 같은 인덱스에 +1

for i in range(10001):
    if arr[i] != 0:  # 0보다 큰 요소
        for j in range(arr[i]):  # 해당 인덱스들을 찾아 그 수만큼 출력
            print(i)

# 1. 리스트를 0으로 초기화
# 2. 입력값을 받을 때 입력값과 같은 인덱스에 1씩 더함
# 3. 리스트를 돌면서 0보다 큰 요소를 갖는 인덱스가 있으면
#    인덱스에 저장된 수만큼 인덱스를 출력
