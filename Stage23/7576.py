M, N = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

from collections import deque
Q = deque([])

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            Q.append([i, j])

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while Q:
    pop_item = Q.popleft()

    for dir in dirs:
        nx = pop_item[0] + dir[0]
        ny = pop_item[1] + dir[1]

        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if matrix[nx][ny] == -1:
            continue
        if matrix[nx][ny] > 0:
            continue

        matrix[nx][ny] = matrix[pop_item[0]][pop_item[1]] + 1
        Q.append([nx, ny])

answer = -1
for m in matrix:
    if 0 in m:
        answer = 0
if answer:
    for a in matrix:
        for b in a:
            if b > answer:
                answer = b
print(answer - 1)
