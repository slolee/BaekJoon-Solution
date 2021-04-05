N = int(input())

numbers = [1, 2]
for i in range(3, N + 1):
    numbers.append((numbers[-1] + numbers[-2]) % 15746)
print(numbers[N - 1])


