def get_self(n):
    sum = n
    for i in str(n):
        sum += int(i)
    return sum

lst = []
for i in range(1, 10000):
    lst.append(get_self(i))
for i in range(1, 10001):
    if i not in lst:
        print(i)