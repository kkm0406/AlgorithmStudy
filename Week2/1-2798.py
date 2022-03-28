n, m = map(int, input().split())
card = list(map(int, input().split()))
sum = 0
for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            tmp = (card[i] + card[j] + card[k])
            if m >= tmp >= sum:
                sum = tmp
print(sum)
