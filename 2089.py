import sys

n = int(sys.stdin.readline())

ret = ""
if n == 0:
    print(0)
    exit(0)
while n:
    if n % (-2):
        ret = "1" + ret
        n = n // -2 + 1
    else:
        ret = "0" + ret
        n //= -2

print(ret)
