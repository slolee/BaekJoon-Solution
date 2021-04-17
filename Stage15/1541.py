# s = input().split('-')
# a = [int(eval(c)) * -1 for c in s]
# a[0] *= -1
# print(sum(a))

s = input()
items = []
s_tmp = ''
for c in s:
    if c in ['+', '-']:
        if s_tmp:
            items.append(s_tmp)
            s_tmp = ''
        items.append(c)
    else:
        s_tmp += c
items.append(s_tmp)

items_2 = []
stack = []
for item in items:
    if item == '+':
        while stack and stack[-1] == '+':
            items_2.append(stack.pop())
        stack.append(item)
    elif item == '-':
        while stack:
            items_2.append(stack.pop())
        stack.append(item)
    else:
        items_2.append(item)
while stack:
    items_2.append(stack.pop())

stack = []
for item in items_2:
    if item == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif item == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else:
        stack.append(int(item))
print(stack.pop())

