def w(a, b, c):
    global mem
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return mem[20][20][20]
    elif a < b < c:
        return mem[a][b][c - 1] + mem[a][b - 1][c - 1] - mem[a][b - 1][c]
    else:
        return mem[a - 1][b][c] + mem[a - 1][b - 1][c] + mem[a - 1][b][c - 1] - mem[a - 1][b - 1][c - 1]


mem = []
for a in range(21):
    tmp_mem2 = []
    for b in range(21):
        tmp_mem = []
        for c in range(21):
            tmp_mem = [1] * 21
        tmp_mem2.append(tmp_mem)
    mem.append(tmp_mem2)

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            mem[a][b][c] = w(a, b, c)

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, 1))
    elif a > 20 or b > 20 or c > 20:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, mem[20][20][20]))
    elif a < b < c:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, mem[a][b][c - 1] + mem[a][b - 1][c - 1] - mem[a][b - 1][c]))
    else:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, mem[a - 1][b][c] + mem[a - 1][b - 1][c] + mem[a - 1][b][c - 1] - mem[a - 1][b - 1][c - 1]))



