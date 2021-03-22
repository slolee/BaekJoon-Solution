N = int(input())
array = map(int, input().split())

answer = 0
for i in array:
    if i == 1:
        continue

    if not [j for j in range(2, i) if i % j == 0]:
        answer += 1
print(answer)