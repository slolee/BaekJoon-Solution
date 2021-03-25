def copy_array(start_x, start_y, source):
    for a in range(len(source)):
        for b in range(len(source)):
            answer[start_x + a][start_y + b] = source[a][b]

def star(n):
    if n > N:
        return

    source = []
    for i in range(n // 3):
        source.append(answer[i][:(n // 3)])

    for i_index, i in enumerate(range(0, n, len(source))):
        for j_index, j in enumerate(range(0, n, len(source))):
            if not (i_index == 1 and j_index == 1):
                copy_array(i, j, source)
    star(n * 3)

N = int(input())
answer = [[False] * N for n in range(N)]
answer[0][0] = True
star(3)

for i in answer:
    for j in i:
        if j: print('*', end='')
        else: print(' ', end='')
    print()