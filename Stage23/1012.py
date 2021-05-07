import sys
sys.setrecursionlimit(100000)

next = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def DFS(x, y):
    global items, N, M

    if not items[y][x]:
        return

    items[y][x] = False
    for n in next:
        nx = x + n[0]
        ny = y + n[1]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        DFS(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    items = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        items[y][x] = True

    answer = 0
    for n in range(N):
        for m in range(M):
            if items[n][m]:
                DFS(m, n)
                answer += 1
    print(answer)

