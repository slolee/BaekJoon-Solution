N = int(input())
for _ in range(N):
    items = input()
    stack = []
    flag = True

    for item in items:
        if item == '(':
            stack.append(item)
        else:
            if not stack:
                flag = False
                break
            pop_item = stack.pop()
            if pop_item == ')':
                flag = False
                break
    if stack:
        flag = False
    print('YES' if flag else 'NO')