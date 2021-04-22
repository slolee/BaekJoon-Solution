while True:
    string = input()
    if string == '.':
        break

    stack = []
    answer = True
    for char in string:
        if char not in ['(', ')', '[', ']']:
            continue
        if char in ['(', '[']:
            stack.append(char)
        elif char == ')':
            if not stack:
                answer = False
                break
            pop_char = stack.pop()
            if pop_char != '(':
                answer = False
                break
        elif char == ']':
            if not stack:
                answer = False
                break
            pop_char = stack.pop()
            if pop_char != '[':
                answer = False
                break
    if stack:
        answer = False
    print('yes' if answer else 'no')