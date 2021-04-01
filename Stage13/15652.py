def backtracking(numbers):
    global N, M
    if len(numbers) == M:
        for number in numbers:
            print(number, end=' ')
        print()
        return

    start = max(numbers) if len(numbers) > 0 else 1
    for i in range(start, N + 1):
        numbers.append(i)
        backtracking(numbers)
        numbers.pop()


N, M = map(int, input().split())
backtracking([])
