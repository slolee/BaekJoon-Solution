N = 123456 * 2 + 1
check_array = [True] * N

for i in range(1, N + 1):
    if i == 1:
        check_array[i - 1] = False
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            check_array[i - 1] = False
            break

while True:
    n = int(input())
    if n == 0:
        break

    print(len([i for i in range(n + 1, 2 * n + 1) if check_array[i - 1]]))
