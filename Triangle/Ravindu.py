n = int(input())

points = []

for i in range(n):
    x, y = [int(x) for x in input().split()]
    points.append([x, y])


max = 0
n = len(points)
for j in range(n):
    max_x = 0
    max_y = 0
    for k in range(n):
        if points[j][1] == points[k][1] and j != k:
            if abs(points[j][0]-points[k][0]) > max_x:
                max_x = abs(points[j][0]-points[k][0])
    for p in range(n):
        if points[j][0] == points[p][0] and j != p:
            if abs(points[j][1]-points[p][1]) > max_y:
                max_y = abs(points[j][1]-points[p][1])

    if max_x*max_y > max:
        max = max_x * max_y

print(max)
