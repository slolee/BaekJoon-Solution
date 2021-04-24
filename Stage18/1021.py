N, M = map(int, input().split())
index = list(map(int, input().split()))

from collections import deque
items = deque([i for i in range(1, N + 1)])
answer = 0
for i in index:
    start = 0
    end = len(items) - 1
    current = items.index(i)

    if current - start <= end - current:
        answer += current - start
        items.rotate(-1 * current - start)
        items.popleft()
    elif current - start > end - current:
        answer += end - current + 1
        items.rotate(end - current)
        items.pop()
print(answer)