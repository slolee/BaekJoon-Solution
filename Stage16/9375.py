# 시간초과
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     cloth = {}
#     for _ in range(N):
#         A, B = input().split()
#         if B in cloth:
#             cloth[B] += 1
#         else:
#             cloth[B] = 1
#     keys = list(cloth.keys())
#
#     answer = 0
#     import itertools
#     for i in range(1, len(keys) + 1):
#         for j in itertools.combinations(keys, i):
#             mul = 1
#             for k in j:
#                 mul *= cloth[k]
#             answer += mul
#     print(answer)

T = int(input())
for _ in range(T):
    N = int(input())
    cloth = {}
    for _ in range(N):
        A, B = input().split()
        if B in cloth:
            cloth[B] += 1
        else:
            cloth[B] = 1

    values = list(cloth.values())
    answer = 1
    for value in values:
        answer *= (value + 1)
    print(answer - 1)