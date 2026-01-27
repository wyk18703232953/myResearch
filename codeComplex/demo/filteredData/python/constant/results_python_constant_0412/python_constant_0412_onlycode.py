p = [int(x) + 100 for x in input().strip().split()]
d = [int(x) + 100 for x in input().strip().split()]

minx = min(p[::2])
maxx = max(p[::2])
miny = min(p[1::2])
maxy = max(p[1::2])

grid = [[False] * 201 for _ in range(201)]
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        grid[x][y] = True

minx = min(d[::2])
maxx = max(d[::2])
avgx = sum(d[::2]) // 4
avgy = sum(d[1::2]) // 4
span = (maxx - minx) // 2

for x in range(minx, maxx+1):
    height = span - abs(x - avgx)
    for y in range(avgy - height, avgy + height + 1):
        if grid[x][y]:
            print('YES')
            exit()

print('NO')
