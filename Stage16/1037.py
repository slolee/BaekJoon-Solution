N = int(input())
numbers = list(map(int, input().split()))
answer = 1

sorted_numbers = sorted(numbers, reverse=True)
for i in range(2, 2200000000):
    flag = True
    for number in sorted_numbers:
        if i % number != 0:
            flag = False
            break
    if flag:
        if i in sorted_numbers:
            i *= sorted_numbers[-1]
        print(i)
        break

# for number in sorted_numbers:
#     if answer % number == 0:
#         continue
#     answer *= number
#
# print(answer)