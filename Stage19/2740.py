def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()

def mul_matrix(matrixA, matrixB):
    global A_row, A_col, B_row, B_col

    result = [[0 for _ in range(B_col)] for _ in range(A_row)]
    for i in range(A_row):
        for j in range(B_col):
            for k in range(A_col):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


A_row, A_col = map(int, input().split())
A = []
for _ in range(A_row):
    A.append(list(map(int, input().split())))

B_row, B_col = map(int, input().split())
B = []
for _ in range(B_row):
    B.append(list(map(int, input().split())))

print_matrix(mul_matrix(A, B))

