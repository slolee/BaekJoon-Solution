def power(N, K):
    global m
    if K == 1:
        return N

    tmp = power(N, K // 2)
    if K % 2 == 0:
        return (tmp * tmp) % m
    else:
        return (tmp * tmp * N) % m


m = 1000000007
N, K = map(int, input().split())

factorial = [1] * (N + 1)
for n in range(2, N + 1):
    factorial[n] = (factorial[n - 1] * n) % m


print(factorial[N] * pow(factorial[N - K], m - 2, m) * pow(factorial[K], m - 2, m) % m)