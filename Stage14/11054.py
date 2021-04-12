N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
dp2 = [1] * N

for i in range(len(A)):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                max_value = A[j]

for i in range(len(A) - 1, -1, -1):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            if dp2[i] < dp2[j] + 1:
                dp2[i] = dp2[j] + 1
                max_value = A[j]

answer = [sum(i) - 1 for i in zip(dp, dp2)]
print(max(answer))
