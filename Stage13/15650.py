def backtracking(numbers):
    global N, M
    if len(numbers) == M:
        for number in numbers:
            print(number, end=' ')
        return

    start = max(numbers) if len(numbers) > 0 else 1
    for i in range(start, N + 1):
        if i in numbers:
            continue
        numbers.append(i)
        backtracking(numbers)
        numbers.remove(i)


N, M = map(int, input().split())
backtracking([])
