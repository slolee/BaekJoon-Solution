def UC(a, b):
    while b:
        a, b = b, a % b
    return a

def UC2(a, b):
    return (a * b) // UC(a, b)


N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    print(UC2(A, B))