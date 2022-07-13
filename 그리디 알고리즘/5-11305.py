import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

money = cost[0] * dist[0]
min_cost = cost[0]
for i in range(1, len(cost) - 1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    money += min_cost * dist[i]

print(money)
