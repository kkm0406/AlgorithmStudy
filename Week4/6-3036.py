import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
num = arr[0]


def find(a, b):
    if b == 0:
        return a
    else:
        return find(b, a % b)


for i in range(1, len(arr)):
    n1 = max(num, arr[i])
    n2 = min(num, arr[i])
    gcd = find(n1, n2)
    print(str(int(num / gcd)) + '/' + str(int(arr[i] / gcd)))
