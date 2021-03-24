T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    count = 0
    gap = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            count = -1
    elif gap > r1 + r2:
        count = 0
    elif gap == r1 + r2:
        count = 1
    elif gap < r1 + r2:
        max_value = max(r1, r2)
        min_value = min(r1, r2)
        if max_value - gap > min_value:
            count = 0
        elif max_value - gap == min_value:
            count = 1
        elif max_value - gap < min_value:
            count = 2

    print(count)