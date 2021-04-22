import sys
N = int(input())
stack = []

for _ in range(N):
    op = sys.stdin.readline()
    if op.startswith('push'):
        stack.append(int(op.split()[1]))
    elif op.startswith('pop'):
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif op.startswith('size'):
        print(len(stack))
    elif op.startswith('empty'):
        print(0 if len(stack) else 1)
    elif op.startswith('top'):
        if len(stack):
            print(stack[-1])
        else:
            print(-1)