string = input()
result = [-1 for i in range(26)]
for i in string:
    result[ord(i) - 97] = string.index(i)
for i in result:
    print(i, end=' ')