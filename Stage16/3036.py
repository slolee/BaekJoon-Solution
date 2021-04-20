N = int(input())
numbers = list(map(int, input().split()))

import math
for number in numbers[1:]:
    gcd = math.gcd(number, numbers[0])
    print(numbers[0] // gcd, '/', number // gcd, sep='')
