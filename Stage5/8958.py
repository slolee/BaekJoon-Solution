N = int(input())
for i in range(N):
    count = 0
    string = input()

    n = 1
    for j in string:
        if j == 'O':
            count += n
            n += 1
        else:
            n = 1
    print(count)