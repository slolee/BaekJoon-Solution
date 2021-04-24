N = int(input())

from collections import deque
queue = deque([])

for n in range(1, N + 1):
    queue.appendleft(n)

while len(queue) > 1:
    queue.pop()
    item = queue.pop()
    queue.appendleft(item)
print(queue[0])