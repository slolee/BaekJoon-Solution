T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    answer = 1
    for i in range(M, M - N, -1):
        answer *= i
    for i in range(1, N + 1):
        answer //= i
    print(answer)
