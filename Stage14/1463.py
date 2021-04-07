N = int(input())
answer = []

for i in range(0, N + 1):
    if i < 2:
        answer.append(0)
    else:
        min_list = []
        if i % 2 == 0:
            min_list.append(answer[i // 2])
        if i % 3 == 0:
            min_list.append(answer[i // 3])
        min_list.append(answer[i - 1])
        answer.append(min(min_list) + 1)
print(answer[N])

