N, K = map(int, input().split())
items = []
for i in range(N):
    items.append(int(input()))
items.reverse()

answer = 0
for item in items:
    while K >= item:
        K -= item
        answer += 1
print(answer)
