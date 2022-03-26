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
