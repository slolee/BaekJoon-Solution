N, M = map(int, input().split())
matrix = []
for _ in range(N):
    items = input()
    matrix.append([bool(int(item)) for item in items])
matrix_tmp = [[0] * M for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from collections import deque
Q = deque([[0, 0]])
matrix_tmp[0][0] = 1

answer = []
while len(Q):
    pop_item = Q.popleft()
    if pop_item[0] == N - 1 and pop_item[1] == M - 1:
        answer.append(pop_item)
        continue

    for i in range(len(dirs)):
        nx = pop_item[0] + dirs[i][0]
        ny = pop_item[1] + dirs[i][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not matrix[nx][ny]:
            continue

        if not matrix_tmp[nx][ny] or matrix_tmp[pop_item[0]][pop_item[1]] + 1 < matrix_tmp[nx][ny]:
            matrix_tmp[nx][ny] = matrix_tmp[pop_item[0]][pop_item[1]] + 1
            Q.append([nx, ny])
print(matrix_tmp[N - 1][M - 1])
