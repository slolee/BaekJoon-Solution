def div_number(k, n):
    print('=== ', k, n, ' ===')
    count = 0
    while k != 0:
        print(k)
        k = k // n
        count += k
    print(count)
    return count


N, M = map(int, input().split())
print(min(div_number(N, 5) - div_number(M, 5) - div_number(N - M, 5), div_number(N, 2) - div_number(M, 2) - div_number(N - M, 2)))