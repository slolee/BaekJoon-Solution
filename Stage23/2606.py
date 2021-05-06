def BFS():
    global matrix, visit, answer

    from collections import deque
    Q = deque([1])

    while len(Q):
        pop = Q.popleft()
        if visit[pop]:
            continue

        visit[pop] = True
        answer += 1
        Q.extend([i for i in range(1, N + 1) if matrix[pop][i]])


N = int(input())
M = int(input())
matrix = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = True

visit = [False] * (N + 1)
answer = 0
BFS()
print(answer - 1)
