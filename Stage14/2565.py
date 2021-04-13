N = int(input())
lst = []
check = {}
for n in range(N):
    lst.append(list(map(int, input().split())))
    check[lst[-1][0]] = 0

sorted_lst = sorted(lst, key=lambda x: x[0])

dp = [1] * N
for i in range(len(sorted_lst)):
    for j in range(i):
        if sorted_lst[i][1] > sorted_lst[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])
print(N - max(dp))


# 겹치는 수 세서 많이 겹치는거부터 지우는 방식해서 총 겹친수에서 뺌
# dp = []
# for i in range(len(sorted_lst)):
#     cnt = 0
#     for j in range(i):
#         if sorted_lst[i][1] < sorted_lst[j][1]:
#             check[sorted_lst[i][0]] += 1
#             check[sorted_lst[j][0]] += 1
#             cnt += 1
#     if i > 0:
#         cnt += dp[-1]
#     dp.append(cnt)
#
# sorted_check = sorted(check.items(), key=lambda x: x[1], reverse=True)
#
# tmp = dp[-1]
# cnt = 0
# for i in sorted_check:
#     tmp -= i[1]
#     cnt += 1
#     if tmp <= 0:
#         print(cnt)
#         break
