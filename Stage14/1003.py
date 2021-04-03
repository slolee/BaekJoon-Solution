answer = [(0, 0) for _ in range(41)]
answer[0] = (1, 0)
answer[1] = (0, 1)
for i in range(2, len(answer)):
    answer[i] = (answer[i - 1][0] + answer[i - 2][0], answer[i - 1][1] + answer[i - 2][1])

T = int(input())
for t in range(T):
    N = int(input())
    print(answer[N][0], answer[N][1])