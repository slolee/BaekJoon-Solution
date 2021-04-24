def printItems(x, y, size):
    global items_2d
    for items in items_2d[x:x + size]:
        for item in items[y:y + size]:
            print(item, end=' ')
        print()

def checkItems(x, y, size):
    global items_2d
    init = items_2d[x][y]
    for items in items_2d[x:x + size]:
        for item in items[y:y + size]:
            if init != item:
                return 9
    return init

def solution(x, y, size):
    global items_2d, minus_one_count, one_count, zero_count
    if size < 1:
        return

    check = checkItems(x, y, size)
    if check == -1:
        minus_one_count += 1
        return
    elif check == 0:
        zero_count += 1
        return
    elif check == 1:
        one_count += 1
        return

    gap = size // 3
    solution(x, y, gap)
    solution(x, y + gap, gap)
    solution(x, y + gap + gap, gap)
    solution(x + gap, y, gap)
    solution(x + gap, y + gap, gap)
    solution(x + gap, y + gap + gap, gap)
    solution(x + gap + gap, y, gap)
    solution(x + gap + gap, y + gap, gap)
    solution(x + gap + gap, y + gap + gap, gap)


N = int(input())
items_2d = []
for n in range(N):
    items_2d.append(list(map(int, input().split())))

minus_one_count, one_count, zero_count = 0, 0, 0
solution(0, 0, N)
print(minus_one_count)
print(zero_count)
print(one_count)