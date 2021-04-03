def solution(cur):
    global N, start_links, isUsed
    global start_team, link_team, answer

    if cur == N // 2:
        link_sum, start_sum = 0, 0
        for i in range(N):
            if i not in start_team:
                for j in link_team:
                    link_sum += start_links[i][j] + start_links[j][i]
                link_team.append(i)
            else:
                for j in start_team:
                    if i >= j:
                        continue
                    # print(i, j, '=', start_links[i][j], start_links[j][i])
                    start_sum += start_links[i][j] + start_links[j][i]

        # print(start_team, link_team, start_sum, link_sum, abs(start_sum - link_sum))
        answer = min(abs(start_sum - link_sum), answer)
        link_team.clear()
        return

    for i in range(max(start_team) if start_team else 0, len(start_links)):
        if isUsed[i]:
            continue

        start_team.append(i)
        isUsed[i] = True
        solution(cur + 1)
        start_team.pop()
        isUsed[i] = False


N = int(input())
start_links = []
for n in range(N):
    start_links.append(list(map(int, input().split())))
isUsed = [False] * len(start_links)

answer = 9999999999
start_team = []
link_team = []
solution(0)
print(answer)