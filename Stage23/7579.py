def printTomato(matrix):
    for i in range(H):
        for j in range(N):
            print(matrix[i][j])
        print()
    print('-' * 30)

def checkMatrix(matrix):
    for i in range(H):
        for j in range(N):
            if 0 in matrix[i][j]:
                return False
    return True


M, N, H = map(int, input().split())
matrix = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    matrix.append(tmp)

from collections import deque
Q = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                Q.append([i, j, k])

dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
while Q:
    pop_item = Q.popleft()

    for dir in dirs:
        nx = pop_item[0] + dir[0]
        ny = pop_item[1] + dir[1]
        nz = pop_item[2] + dir[2]

        if not (0 <= nx < H and 0 <= ny < N and 0 <= nz < M):
            continue
        if matrix[nx][ny][nz] == -1:
            continue
        if matrix[nx][ny][nz] > 0:
            continue

        matrix[nx][ny][nz] = matrix[pop_item[0]][pop_item[1]][pop_item[2]] + 1
        Q.append([nx, ny, nz])

if checkMatrix(matrix):
    answer = 0
    for i in range(H):
        for j in range(N):
            answer = max(answer, max(matrix[i][j]))
    print(answer - 1)
else:
    print(-1)