answer = [1, 1, 1, 2, 2]

for i in range(5, 100):
    answer.append(answer[i - 1] + answer[i - 5])


T = int(input())
for t in range(T):
    N = int(input())
    print(answer[N - 1])

    