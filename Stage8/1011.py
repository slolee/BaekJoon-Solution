T = int(input())
for t in range(T):
    x, y = map(int, input().split())

    start = 0
    end = y - x
    move = 0
    count = 0

    while start < end:
        if end - start <= move + 1:
            count += 1
            break
        move += 1
        start += move
        end -= move
        count += 2

    print(count)

