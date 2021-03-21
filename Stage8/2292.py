N = int(input())
answer = 1

temp, count = 0, 1
while N != 1 and N > count:
    temp += 6
    count += temp
    answer += 1
print(answer)