def get_number(current):
    global N, M

    if len(current) == M:
        for n in current:
            print(n, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if i in current:
            continue
        current.append(i)
        get_number(current)
        current.remove(i)


N, M = map(int, input().split())
get_number([])
