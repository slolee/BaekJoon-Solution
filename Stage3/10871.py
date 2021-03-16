N, X = map(int, input().split(' '))
print(' '.join(map(str, filter(lambda n: n < X, map(int, input().split(' '))))))
