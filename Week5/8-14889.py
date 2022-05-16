N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = int(1e9)
team1 = []


def cal_diff(team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


def make_team(count, start):
    global answer

    if count == N // 2:
        team2 = []
        for i in range(N):
            if i not in team1: #team1에 없으면 team2
                team2.append(i)

        local_diff = cal_diff(team2) #팀 능력치 차를 구함
        answer = min(answer, local_diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i) #dfs를 사용해서 선택
            make_team(count + 1, i + 1)
            team1.remove(i)


make_team(0, 0)

print(answer)
