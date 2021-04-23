N = int(input())
numbers = list(map(int, input().split()))

# 시간초과
# for i in range(N):
#     flag = False
#     for j in range(i + 1, N):
#         if numbers[i] < numbers[j]:
#             print(numbers[j], end=' ')
#             flag = True
#             break
#     if not flag:
#         print('-1', end=' ')

