N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

stack = []
cnt = 0
answer = ''
for n in range(1, N + 1):
    stack.append(n)
    answer += '+\n'
    while stack and numbers[cnt] == stack[-1]:
        cnt += 1
        stack.pop()
        answer += '-\n'

if stack:
    print('NO')
else:
    print(answer)
