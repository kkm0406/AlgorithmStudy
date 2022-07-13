n = input()

n = n.split('-')


for i in range(len(n)):
    n[i] = n[i].split('+')
    n[i] = list(map(int, n[i]))
    n[i] = sum(n[i])


for i in range(1, len(n)):
    n[i] = n[i-1] - n[i]

print(n[-1])


