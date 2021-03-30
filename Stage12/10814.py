import sys

N = int(input())
users = []
for n in range(N):
    age, name = sys.stdin.readline().split()
    users.append((int(age), name))

for i in sorted(users, key=lambda x: x[0]):
    sys.stdout.write(str(i[0]) + ' ' + i[1] + '\n')