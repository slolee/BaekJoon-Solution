A, B = input().split(' ')
# print(max(int(''.join([A[a] for a in range(len(A) - 1, -1, -1)])), int(''.join([B[b] for b in range(len(B) - 1, -1, -1)]))))
print(max(int(A[::-1]), int(B[::-1])))
