def backtracking(numbers):
    global N, M
    if len(numbers) == M:
        for number in numbers:
            print(number, end=' ')
        print()
        return

    for i in range(1, N + 1):
        numbers.append(i)
        backtracking(numbers)
        numbers.pop()


N, M = map(int, input().split())
backtracking([])
