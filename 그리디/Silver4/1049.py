import math
import sys

N, M = map(int, sys.stdin.readline().split())
package = 1000
single = 1000
money = 10000000

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if package > a:
        package = a
    if single > b:
        single = b

for i in range(0, math.ceil(N / 6) + 1):
    result = package * i
    if N - (i * 6) >= 0:
        result += single * (N - i * 6)
    if money > result:
        money = result

print(money)
