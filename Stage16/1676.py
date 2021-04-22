N = int(input())
two_cnt = 0
five_cnt = 0
for n in range(1, N + 1):
    while n % 2 == 0:
        two_cnt += 1
        n //= 2
    while n % 5 == 0:
        five_cnt += 1
        n //= 5

print(min(two_cnt, five_cnt))
