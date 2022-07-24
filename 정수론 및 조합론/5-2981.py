import sys
from math import gcd
from math import sqrt

n = int(sys.stdin.readline())
ls = []
result = []

for _ in range(n):
    ls.append(int(sys.stdin.readline()))
ls.sort()  # 오름차순 정렬

temp = [ls[i] - ls[i - 1] for i in range(1, n)]  # 각 인접 요소들끼리 뺄셈
my_gcd = temp[0]  # 리스트 내 모든 요소들의 gcd를 구하기 위함

for i in range(1, n - 1):
    my_gcd = gcd(my_gcd, temp[i])

for i in range(1, int(sqrt(my_gcd)) + 1): #최대공약수를 찾기 위해 제곱근까지만 탐색
    if my_gcd % i == 0:
        if i ** 2 == my_gcd:
            result.append(i)
        else:
            result += [i, my_gcd // i]
result.remove(1)
result.sort()

for i in range(len(result)):
    print(result[i], end=" ")

#나머지가 같은 수의 집합체는 큰 수부터 정렬했을 때, 두 수의 차이가 일정
# A = M * a + R
# B = M * b + R
# C = M * c + R
# 여기서 R을 제거하면
# A - B = M(a - b)
# B - C = M(b - c)
# 이런 식이 나온다.
#a, b, c, d의 나머지가 같을 수를 구할 때 a-b, b-c, c-d의 최대공약수를 구함
#먼저 두개의 수를 골라 최대공약수를 구한 수 그 최대공약수와 남은 수의 최대공약수를 구함