n = list(map(int, input()))

for i in range(len(n)-1):
    idx = i
    for j in range(i+1, len(n)):
        if n[idx] < n[j]:
            n[idx], n[j] = n[j], n[idx]

ret = ""

for i in n:
    ret += str(i)

print(ret)
