import sys
N = int(input())

numbers = []
for n in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for number in numbers:
    sys.stdout.write(str(number) + '\n')