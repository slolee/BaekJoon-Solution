max, index = 0, -1
for i in range(9):
    n = int(input())
    if n > max:
        index = i
        max = n
print(max)
print(index + 1)