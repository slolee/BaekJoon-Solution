N = int(input())
numbers_triangle = []
answer = []
for n in range(N):
    numbers = list(map(int, input().split()))

    if n == 0:
        answer.append(numbers)
    else:
        temp = []
        for index, number in enumerate(numbers):
            if index == 0:
                temp.append(number + answer[-1][index])
            elif index == len(numbers) - 1:
                temp.append(number + answer[-1][index - 1])
            else:
                temp.append(number + max(answer[-1][index - 1], answer[-1][index]))
        answer.append(temp)
print(max(answer[-1]))
