def check_solution(start):
    global check_queen
    if check_queen[chess[start]]:
        return False

    for i in range(1, start + 1):
        if not check_queen[chess[start - i]]:
            break
        if chess[start - i] == chess[start] + i or chess[start - i] == chess[start] - i:
            return False
    return True


def solution(start):
    global N, answer, check_queen

    if chess.count(-1) == 0:
        answer += 1
        return

    for i in range(N):
        chess[start] = i

        if not (check_solution(start)):
            chess[start] = -1
            continue
        check_queen[i] = True
        solution(start + 1)
        chess[start] = -1
        check_queen[i] = False


N = int(input())
answer = 0
check_queen = [False] * N
chess = [-1] * N
solution(0, )
print(answer)
