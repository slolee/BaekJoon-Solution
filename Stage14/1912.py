N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N
dp[0] = numbers[0]
for n in range(1, len(numbers)):
    dp[n] = max(numbers[n], dp[n - 1] + numbers[n])
print(max(dp))
