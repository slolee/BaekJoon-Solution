N, K = map(int, input().split())

from collections import deque
queue = deque([i for i in range(1, N + 1)])

answer = []
while queue:
    queue.rotate(-1 * K)
    answer.append(queue.pop())
print('<', ', '.join(map(str, answer)), '>', sep='')