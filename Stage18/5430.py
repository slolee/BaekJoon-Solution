import sys
from collections import deque

for _ in range(int(input())):
    ops = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()

    lst = deque([])
    if arr != '[]\n':
        lst.extend(list(map(int, arr[1:-2].split(','))))

    isError = False
    left = True
    for op in ops:
        if op == 'R':
            left = not left
        elif op == 'D':
            if not lst:
                isError = True
                break
            if left:
                lst.popleft()
            else:
                lst.pop()
    if isError:
        print('error')
    else:
        if left:
            print('[', ','.join(list(map(str, lst))), ']', sep='')
        else:
            print('[', ','.join(list(map(str, reversed(lst)))), ']', sep='')
