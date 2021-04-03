def check_solution(start, value):
    global check_queen
    if check_queen[value]:
        return False

    for i in range(1, start + 1):
        if not check_queen[chess[start - i]]:
            break
        if chess[start - i] == value + i or chess[start - i] == value - i:
            return False
    return True


def solution(start):
    global N, answer, check_queen

    if start == N:
        answer += 1
        return

    for i in range(N):
        if not (check_solution(start, i)):
            continue
        chess[start] = i
        check_queen[i] = True
        solution(start + 1)
        check_queen[i] = False


N = int(input())
answer = 0
check_queen = [False] * N
chess = [-1] * N
solution(0, )
print(answer)
