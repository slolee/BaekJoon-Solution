M = int(input())
N = int(input())

total, minimum = 0, 0
for i in range(M, N + 1):
    if i == 1:
        continue
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        if total == 0:
            minimum = i
        total += i
if total == 0:
    print(-1)
else:
    print(total)
    print(minimum)
