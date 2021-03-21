A, B, V = map(int, input().split())

answer = 1
days = A - B

V -= A
if V % days != 0:
    answer += 1
answer += V // days

print(answer)
