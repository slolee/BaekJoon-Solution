N = int(input())
max1 = -1000001
min1 = 1000001
n = map(int, input().split(' '))
for i in n:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i

print(min1, max1)