import sys

a, b = map(int, sys.stdin.readline().split())


def fact(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num


print(int(fact(a) / (fact(b) * fact(a - b))))
