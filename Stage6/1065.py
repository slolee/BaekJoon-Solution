def get_hansu(N):
    if N < 10:
        return True
    lst = list(map(int, str(N)))
    lst2 = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]
    return True if lst2.count(lst2[0]) == len(lst2) else False

print(len(list(filter(lambda x: get_hansu(x), range(1, int(input()) + 1)))))
