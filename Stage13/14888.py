def solution(cur):
    global N, numbers, operators_tmp, operators, max_value, min_value

    if cur == N - 1:
        answer = numbers[0]
        for i in range(1, len(numbers)):
            if operators[i - 1] == '+':
                answer += numbers[i]
            if operators[i - 1] == '-':
                answer -= numbers[i]
            if operators[i - 1] == '*':
                answer *= numbers[i]
            if operators[i - 1] == '/':
                if answer < 0:
                    answer = (abs(answer) // numbers[i]) * -1
                else:
                    answer //= numbers[i]
        max_value = max(max_value, answer)
        min_value = min(min_value, answer)
        return

    for i in range(len(operators_tmp)):
        if isUsed[i]:
            continue
        operators.append(operators_tmp[i])
        isUsed[i] = True
        solution(cur + 1)
        operators.pop()
        isUsed[i] = False


N = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

operators_tmp = []
operators_tmp.extend(['+'] * operators_count[0])
operators_tmp.extend(['-'] * operators_count[1])
operators_tmp.extend(['*'] * operators_count[2])
operators_tmp.extend(['/'] * operators_count[3])
# print(operators_tmp)
isUsed = [False] * len(operators_tmp)
max_value = -1000000000
min_value = 1000000000

operators = []
solution(0)
print(max_value)
print(min_value)
