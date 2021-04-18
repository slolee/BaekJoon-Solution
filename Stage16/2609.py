def UC(a, b):
    while b:
        a, b = b, a % b
    return a

def UC2(a, b):
    return (a * b) // UC(a, b)

A, B = map(int, input().split())
print(UC(A, B))
print(UC2(A, B))