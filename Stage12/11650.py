N = int(input())

points = []
for n in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

for x, y in sorted(sorted(points, key=lambda a: a[1]), key=lambda a: a[0]):
    print(x, y)