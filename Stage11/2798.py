def bf(start, array):
    global  answer
    total = sum(array)
    if len(array) == 3:
        if M >= total > answer:
            answer = total
        return

    for i in range(start, len(cards)):
        array.append(cards[i])
        bf(i + 1, array)
        array.remove(cards[i])


N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
bf(0, [])
print(answer)

