N = int(input())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

items = sorted(sorted(items, key=lambda x: x[0]), key=lambda x: x[1])

start_time = 0
answer = [[0, 0]]
for item in items:
    if answer[-1][1] <= item[0]:
        answer.append(item)
print(len(answer) - 1)