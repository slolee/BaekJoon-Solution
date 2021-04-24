import sys
from collections import deque

queue = deque([])
for _ in range(int(input())):
    op = sys.stdin.readline().split()

    if op[0] == 'push_front':
        queue.appendleft(op[1])
    elif op[0] == 'push_back':
        queue.append(op[1])
    elif op[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif op[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        print(0 if queue else 1)
    elif op[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif op[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
