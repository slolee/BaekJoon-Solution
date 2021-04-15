N, K = map(int, input().split())
item = []
for n in range(N):
    item.append(tuple(map(int, input().split())))

dp = [[0] * K for _ in range(N)]
for n in range(N):
    for k in range(K):
        if item[n][0] <= k + 1:
            if n > 0:
                if k - item[n][0] > 0:
                    dp[n][k] = max(dp[n - 1][k], item[n][1] + dp[n - 1][k - item[n][0]])
                else:
                    dp[n][k] = max(dp[n - 1][k], item[n][1])
            else:
                dp[n][k] = item[n][1]
        else:
            if n > 0:
                dp[n][k] = dp[n - 1][k]

print(dp[N - 1][K - 1])