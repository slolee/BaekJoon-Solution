N = int(input())
score = list(map(int, input().split(' ')))
max = 0
for i in range(N):
    if score[i] >= max:
        max = score[i]

new_score = map(lambda x: x / max * 100, score)
print(sum(new_score) / N)