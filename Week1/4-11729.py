n = int(input())
arr = []


def hanoi(num, src, tmp, dst):
    if num == 1:
        arr.append(src+' '+dst)
        return
    else:
        hanoi(num - 1, src, dst, tmp)
        arr.append(src+' '+dst)
        hanoi(num - 1, tmp, src, dst)


hanoi(n, '1', '2', '3')
print(len(arr))
for i in arr:
    print(i)


# 하노이 탑, 실버 1

n = int(input())


def Hanoi(n, a, c):
    if n == 1:
        print(a, c)
        return
    Hanoi(n - 1, a, 6 - a - c)  # a번 막대를 1, c번 막대를 3 이라 했을 때, a + b + c = 6이므로, 6-a-c 값은 원판이 이동 할 막대의 번호
    print(a, c)
    Hanoi(n - 1, 6 - a - c, c)


print(2 ** n - 1)
Hanoi(n, 1, 3)