import sys
N = int(input())

count = {}
for n in range(N):
    number = int(sys.stdin.readline())
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

for number in sorted(count):
    for i in range(count[number]):
        print(number)
