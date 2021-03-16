T = int(input())
for t in range(T):
    input_value = input().split(' ')
    count = int(input_value[0])
    string = input_value[1]

    for i in string:
        print(i * count, end='')
    print()