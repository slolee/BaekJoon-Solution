def print_numbers(numbers):
    for number in numbers:
        for n in number:
            print(n, end=' ')
        print()
    print()


def check_sdoku(zero_numbers, j):
    global numbers
    # 가로
    x = zero_numbers[0]
    y = zero_numbers[1]

    for number in numbers[x]:
        if number == j:
            return False
    for numbers_2 in numbers:
        if numbers_2[y] == j:
            return False

    start_x = x // 3 * 3
    start_y = y // 3 * 3
    for xx in range(start_x, start_x + 3):
        for yy in range(start_y, start_y + 3):
            if numbers[xx][yy] == j:
                return False
    return True


def is_clear(numbers):
    for i in range(9):
        for j in range(9):
            if numbers[i][j] == 0:
                return False
    return True


def solution(start, result):
    global zero_numbers, numbers

    if len(result) == len(zero_numbers):
        print_numbers(numbers)
        exit()

    # for i in range(start, len(zero_numbers)):
    for j in range(1, 10):
        if not check_sdoku(zero_numbers[start], j):
            if j == 9:
                break
            continue
        result.append(zero_numbers[start])
        numbers[zero_numbers[start][0]][zero_numbers[start][1]] = j
        solution(start + 1, result)
        numbers[zero_numbers[start][0]][zero_numbers[start][1]] = 0
        result.pop()


numbers = []
zero_numbers = []

for i in range(9):
    numbers.append(list(map(int, input().split())))
    for j in range(len(numbers[-1])):
        if numbers[i][j] == 0:
            zero_numbers.append((i, j))
# print(zero_numbers)
solution(0, [])
