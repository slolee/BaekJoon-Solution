lst = []
for i in range(10):
    n = int(input()) % 42
    if n not in lst:
        lst.append(n)
print(len(lst))