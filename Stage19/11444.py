def printMatrix(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            print(_matrix[i][j], end=' ')
        print()


def mulMatrix(matrixA, matrixB):
    global m
    result = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrixA[i][k] * matrixB[k][j] % m
    return result


def solution(_matrix, n):
    if n == 1:
        return _matrix

    temp = solution(_matrix, n // 2)
    if n % 2 == 0:
        return mulMatrix(temp, temp)
    else:
        return mulMatrix(mulMatrix(temp, temp), _matrix)


B = int(input())
m = 1000000007
matrix = [[1, 1], [1, 0]]
print(solution(matrix, B)[0][1] % m)

