N = int(input())
N_tmp = N
count = 0
while True:
    n1 = 0 if N_tmp < 10 else N_tmp // 10
    n2 = N_tmp % 10

    count += 1
    N_tmp = ((n1 + n2) % 10) + n2 * 10
    if N == N_tmp:
        print(count)
        break
