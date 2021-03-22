N = int(input())
for i in range(N // 5, -1, -1):
    tmp = N - (i * 5)
    if tmp % 3 == 0:
        print(i + (tmp // 3))
        break
    if i == 0:
        print(-1)