N = 10000
check_array = [True] * N

for i in range(1, N + 1):
    if i == 1:
        check_array[i - 1] = False
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            check_array[i - 1] = False
            break

T = int(input())
for t in range(T):
    n = int(input())

    x, y = 0, 0
    gap_min = 10000
    for i in range(2, n // 2 + 1):
        if check_array[i - 1] and check_array[n - i - 1]:
            if gap_min > n - i - i:
                x, y = i, n - i
                gap_min = y - x
    print(x, y)


