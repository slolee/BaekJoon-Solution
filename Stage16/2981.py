N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

sub_numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

import math
if len(sub_numbers) > 1:
    gcd = math.gcd(sub_numbers[0], sub_numbers[1])
    for i in range(2, len(sub_numbers)):
        gcd = math.gcd(gcd, sub_numbers[i])
else:
    gcd = sub_numbers[0]

for i in range(2, gcd + 1):
    if gcd % i == 0:
        print(i, end=' ')