N = int(input())
dp = [0]
numbers = [0]
for n in range(N):
    numbers.append(int(input()))

dp.append(numbers[1])
if N > 1:
    dp.append(numbers[1] + numbers[2])

for n in range(3, N + 1):
    dp.append(max(dp[n - 1], dp[n - 2] + numbers[n], dp[n - 3] + numbers[n - 1] + numbers[n]))

print(dp[N])