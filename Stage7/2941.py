string = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for char in lst:
    string = string.replace(char, '?')
print(len(string))