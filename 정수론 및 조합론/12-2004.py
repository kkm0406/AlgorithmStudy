import sys

n, m = map(int, sys.stdin.readline().split())


def count(num, k):
    cnt = 0
    while num:
        num //= k
        cnt += num
    return cnt


five = count(n, 5) - count(m, 5) - count((n - m), 5)
two = count(n, 2) - count(m, 2) - count((n - m), 2)

print(min(five, two))

#fact를 직접 구하거나 조합을 구하면 시간/메모리 초과
#a^m / a^n = a^(m-n)
#0의 개수는 M!이 가지고 있는 2의 개수-N!이 가지고 있는 2의 개수-(M-N)!이 가지고 있는 0의 개수
#10은 2*5이므로 0의 개수는 해당 숫자가 2와 5로 나누어 지는 횟수 중 최소값