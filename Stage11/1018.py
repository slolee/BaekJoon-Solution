N, M = map(int, input().split())
chess = []
check = []
for i in range(8):
    check.append([False] * 8)

white_start = 'WBWBWBWB'
black_start = 'BWBWBWBW'

for n in range(N):
    chess.append(input())

min_count = 9999
for start_index_x in range(N - 7):
    for start_index_y in range(M - 7):
        start_color = chess[start_index_x][start_index_y]

        count = 0
        for i in range(8):
            if i % 2 == 0:
                count += len([0 for x, y in zip(chess[start_index_x + i][start_index_y:start_index_y + 8], white_start) if x != y])
            elif i % 2 == 1:
                count += len([0 for x, y in zip(chess[start_index_x + i][start_index_y:start_index_y + 8], black_start) if x != y])
        if min_count >= count:
            min_count = count

        count = 0
        for i in range(8):
            if i % 2 == 1:
                count += len([0 for x, y in zip(chess[start_index_x + i][start_index_y:start_index_y + 8], white_start) if x != y])
            elif i % 2 == 0:
                count += len([0 for x, y in zip(chess[start_index_x + i][start_index_y:start_index_y + 8], black_start) if x != y])
        if min_count >= count:
            min_count = count

print(min_count)