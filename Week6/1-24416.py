import sys

n = int(sys.stdin.readline())


def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


fib = [0] * n
cnt2 = 0


def fib2(num):
    fib[0] = 1
    fib[1] = 1
    global cnt2
    for i in range(2, num):
        cnt2 += 1
        fib[i] = fib[i - 1] + fib[i - 2]


#
fib2(n)

print(fib1(n), cnt2)
