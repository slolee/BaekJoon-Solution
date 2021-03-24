x_point = []
y_point = []
for t in range(3):
    x, y = map(int, input().split())
    if x in x_point:
        x_point.remove(x)
    else:
        x_point.append(x)

    if y in y_point:
        y_point.remove(y)
    else:
        y_point.append(y)

print(x_point[0], y_point[0])