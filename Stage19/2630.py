def printItems(x, y, size):
    global items_2d
    for items in items_2d[x:x + size]:
        for item in items[y:y + size]:
            print(item, end=' ')
        print()

def checkItems(x, y, size):
    global items_2d
    result = items_2d[x][y]
    for items in items_2d[x:x + size]:
        for item in items[y:y + size]:
            if item != result:
                return -1
    return result

def solution(x, y, size):
    global items_2d, zero_cnt, one_cnt

    check = checkItems(x, y, size)
    if check == 0:
        zero_cnt += 1
        return
    elif check == 1:
        one_cnt += 1
        return

    gap = size // 2
    solution(x, y, gap)
    solution(x + gap, y, gap)
    solution(x, y + gap, gap)
    solution(x + gap, y + gap, gap)


N = int(input())
items_2d = []
for n in range(N):
    items_2d.append(list(map(int, input().split())))

zero_cnt, one_cnt = 0, 0
solution(0, 0, N)
print(zero_cnt)
print(one_cnt)
