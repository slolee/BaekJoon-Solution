N = int(input())
numbers = []
for n in range(N):
    numbers.append(int(input()))

if N > 2:
    one_step = [numbers[0], numbers[0] + numbers[1]]
    two_step = [0, numbers[1]]

    for i in range(2, len(numbers)):
        one_step.append(two_step[i - 1] + numbers[i])
        two_step.append(max(one_step[i - 2], two_step[i - 2]) + numbers[i])

    print(max(one_step[-1], two_step[-1]))
else:
    if N == 1:
        print(numbers[0])
    else:
        print(max(numbers[1], numbers[0] + numbers[1]))