N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(len(A)):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                max_value = A[j]

print(max(dp))
