import math

m, n = map(int, input().split())


def f(num):
    if num == 1:
        return False
    else:
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
        return True


for i in range(m, n + 1):
    if f(i):
        print(i)
