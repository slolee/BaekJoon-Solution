N = int(input())
i = 665
answer = 0
while answer < N:
    if str(i).find('666') != -1:
        answer += 1
    i += 1
print(i - 1)