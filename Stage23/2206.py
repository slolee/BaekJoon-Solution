N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([bool(int(item)) for item in input()])

matrix_status = [[[0, 0] for _ in range(M)] for _ in range(N)]
from collections import deque
Q = deque([[0, 0, 0]])

matrix_status[0][0][0] = 1

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while Q:
    pop_item = Q.popleft()
    for dir in dirs:
        nx = pop_item[0] + dir[0]
        ny = pop_item[1] + dir[1]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if not matrix[nx][ny]:
            if matrix_status[nx][ny][pop_item[2]] == 0:
                matrix_status[nx][ny][pop_item[2]] = matrix_status[pop_item[0]][pop_item[1]][pop_item[2]] + 1
                Q.append([nx, ny, pop_item[2]])
        else:
            if pop_item[2] == 0 and matrix_status[nx][ny][1] == 0:
                matrix_status[nx][ny][1] = matrix_status[pop_item[0]][pop_item[1]][pop_item[2]] + 1
                Q.append([nx, ny, 1])

if matrix_status[N - 1][M - 1][0] == 0 and matrix_status[N - 1][M - 1][1] == 0:
    print(-1)
elif matrix_status[N - 1][M - 1][0] == 0:
    print(matrix_status[N - 1][M - 1][1])
elif matrix_status[N - 1][M - 1][1] == 0:
    print(matrix_status[N - 1][M - 1][0])
else:
    print(min(matrix_status[N - 1][M - 1]))

