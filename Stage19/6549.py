# while True:
#     buffer = list(map(int, input().split()))
#     N = buffer[0]
#     if N == 0:
#         break
#     items = buffer[1:]
#
#     max_value = 0
#     for i in range(1, max(items) + 1):
#         check = [False] * N
#         for j in range(len(check)):
#             if items[j] >= i:
#                 check[j] = True
#
#         dp = [0] * len(check)
#         dp[0] = 1 if check[0] else 0
#         for j in range(1, len(check)):
#             if check[j]:
#                 dp[j] += dp[j - 1] + 1
#             else:
#                 dp[j] = 0
#
#         tmp = i * max(dp)
#         if tmp > max_value:
#             max_value = tmp
#     print(max_value)


while True:
    buffer = list(map(int, input().split()))
    N = buffer[0]
    if N == 0:
        break
    items = buffer[1:]
