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
    global items_2d, answer

    check = checkItems(x, y, size)
    if check == 0:
        answer += '0'
        return
    elif check == 1:
        answer += '1'
        return

    gap = size // 2

    answer += '('
    solution(x, y, gap)
    solution(x, y + gap, gap)
    solution(x + gap, y, gap)
    solution(x + gap, y + gap, gap)
    answer += ')'


N = int(input())
items_2d = []
for _ in range(N):
    items_2d.append(list(map(int, list(input()))))

answer = ''
solution(0, 0, N)
print(answer)
