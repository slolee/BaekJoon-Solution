N, K = map(int, input().split())
matrix = [0] * 300000

from collections import deque
Q = deque([N])

while Q:
    pop_item = Q.popleft()

    if pop_item == K:
        break

    n1 = pop_item + 1
    if n1 < len(matrix):
        if matrix[n1] == 0 or matrix[pop_item] + 1 < matrix[n1]:
            matrix[n1] = matrix[pop_item] + 1
            Q.append(n1)

    n2 = pop_item - 1
    if 0 <= n2:
        if matrix[n2] == 0 or matrix[pop_item] + 1 < matrix[n2]:
            matrix[n2] = matrix[pop_item] + 1
            Q.append(n2)

    n3 = pop_item * 2
    if n3 < len(matrix):
        if matrix[n3] == 0 or matrix[pop_item] + 1 < matrix[n3]:
            matrix[n3] = matrix[pop_item] + 1
            Q.append(n3)
print(matrix[K])