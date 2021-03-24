while True:
    lst = list(map(int, input().split()))
    if lst.count(0) == 3:
        break

    max_value = max(lst)
    lst.remove(max_value)

    if (lst[0] ** 2 + lst[1] ** 2) == max_value ** 2:
        print('right')
    else:
        print('wrong')