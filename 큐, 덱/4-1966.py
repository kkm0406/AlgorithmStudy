import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    queue = [(v, idx) for idx, v in enumerate(queue)]
    cnt = 0
    while True:
        if max(queue)[0] == queue[0][0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
