N = int(input())
items = list(map(int, input().split()))

items = sorted(items)
answer = 0
for i, item in enumerate(items):
    answer += item * (len(items) - i)
print(answer)