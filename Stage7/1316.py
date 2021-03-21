N = int(input())
answer = 0

for i in range(N):
    string = input()
    temp = []

    current_char = string[0]
    flag = True
    for char in string:
        if current_char == char:
            continue

        if char in temp:
            flag = False
            break
        temp.append(current_char)
        current_char = char

    if flag:
        answer += 1

print(answer)

