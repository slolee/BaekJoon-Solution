T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())

    array = [[1] * (n + 1)]
    for i in range(k + 1):
        array.append([0] * (n + 1))
    for i in range(len(array)):
        if i == 0:
            continue

        for j in range(len(array[i])):
            if j == 0:
                array[i][j] = 0
            else:
                array[i][j] = array[i - 1][j] + array[i][j - 1]
    print(array[k + 1][n])

