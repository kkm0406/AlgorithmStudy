n = int(input())


def makeStar(num):
    arr = []
    if num == 1:
        return ['*']
    star = makeStar(num // 3)
    for i in star:
        arr.append(i * 3)
    for i in star:
        arr.append(i + ' ' * (num // 3) + i)
    for i in star:
        arr.append(i * 3)
    return arr


for i in makeStar(n):
    print(i)
