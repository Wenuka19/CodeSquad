n, k = [int(x) for x in input().split()]


positions = []
categories = []

for i in range(n):
    position, cat = [int(x) for x in input().split()]
    positions.append(position)
    categories.append(cat)

for j in range(len(positions)):
    cats = []
    k = j
    while len(cats)+1 <= k:
        cats.append(categories[k])
