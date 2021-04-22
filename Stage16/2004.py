def div_number(k, n):
    count = 0
    while k != 0:
        k = k // n
        count += k
    return count


N, M = map(int, input().split())
print(min(div_number(N, 5) - div_number(M, 5) - div_number(N - M, 5), div_number(N, 2) - div_number(M, 2) - div_number(N - M, 2)))
