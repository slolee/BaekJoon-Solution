def solution(N):
    global A, C
    if N == 1:
        return A % C

    tmp = solution(N // 2)
    if N % 2 == 0:
        return tmp * tmp % C
    else:
        return tmp * tmp * A % C


A, B, C = map(int, input().split())
answer = solution(B)
print(answer)
