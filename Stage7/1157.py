string = input()
result = {}
for i in string.upper():
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

check = None
for i in result.keys():
    if not check or result[check] < result[i]:
        check = i

if len([i for i in result.keys() if result[i] == result[check]]) > 1:
    print('?')
else:
    print(check)