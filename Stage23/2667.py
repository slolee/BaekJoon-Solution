next = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(x, y):
    global matrix, N, cnt

    if not matrix[x][y]:
        return

    cnt += 1
    matrix[x][y] = False
    for n in next:
        next_x = x + n[0]
        next_y = y + n[1]

        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
            continue
        dfs(next_x, next_y)


N = int(input())
matrix = []
for _ in range(N):
    items = input()
    matrix.append([bool(int(item)) for item in items])

answer = 0
answer_cnt = []
for i in range(N):
    for j in range(N):
        cnt = 0
        dfs(i, j)
        if cnt > 0:
            answer_cnt.append(cnt)
            answer += 1

print(answer)
for cnt in sorted(answer_cnt):
    print(cnt)
