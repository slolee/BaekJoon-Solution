def printMatrix(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            print(_matrix[i][j] % 1000, end=' ')
        print()


def mulMatrix(matrixA, matrixB):
    global N

    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrixA[i][k] * matrixB[k][j] % 1000
    return result


def solution(_matrix, n):
    if n == 1:
        return _matrix

    temp = solution(_matrix, n // 2)
    if n % 2 == 0:
        return mulMatrix(temp, temp)
    else:
        return mulMatrix(mulMatrix(temp, temp), _matrix)


N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
printMatrix(solution(matrix, B))

