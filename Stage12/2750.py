T = int(input())
numbers = []
for t in range(T):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)