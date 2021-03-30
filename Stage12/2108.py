import sys
N = int(input())

numbers = []
bins = {}
for n in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)

    if number in bins:
        bins[number] += 1
    else:
        bins[number] = 1

order_numbers = sorted(numbers)
print(round(sum(numbers) / len(numbers)))
print(order_numbers[len(order_numbers) // 2])

tmp = sorted(sorted(bins.items()), key=lambda x: x[1], reverse=True)
if len(tmp) == 1:
    print(tmp[0][0])
else:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])

print(max(numbers) - min(numbers))