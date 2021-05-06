def DFS(current):
    global matrix, visit_list

    visit_list[current] = True
    print(current, end=' ')
    for i in range(1, N + 1):
        if not visit_list[i] and matrix[current][i]:
            DFS(i)

def BFS():
    global matrix, N, V
    from collections import deque
    Q = deque([])

    visit_list = [False] * (N + 1)
    Q.extend([V])

    while len(Q):
        pop = Q.popleft()
        if visit_list[pop]:
            continue
        print(pop, end=' ')
        visit_list[pop] = True
        Q.extend([i for i in range(1, N + 1) if matrix[pop][i]])


N, M, V = map(int, input().split())
matrix = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = True
    matrix[y][x] = True

visit_list = [False] * (N + 1)
DFS(V)
print()
BFS()