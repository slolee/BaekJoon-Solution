def pibo(x, y, n):
    if n == 0:
        return 0
    if n == 1:
        return y
    return pibo(y, x + y, n - 1)


n = int(input())
print(pibo(0, 1, n))
