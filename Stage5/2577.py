A = int(input())
B = int(input())
C = int(input())
result = A * B * C

num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while result > 0:
    n = result % 10
    result //= 10
    num[n] += 1

for i in num:
    print(i)