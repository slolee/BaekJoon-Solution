from collections import deque

N = int(input())
queue = deque([])

import sys
for _ in range(N):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        queue.insert(0, op[1])
    elif op[0] == 'pop':
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
            print(queue[-1])
        else:
            print(-1)
    elif op[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)
