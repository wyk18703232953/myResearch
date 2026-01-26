n = int(input())

parts = []
for i in range(4):
    part = []
    for _i in range(n):
        part.append([int(x) for x in input()])
    parts.append(part)

    if i < 3:input()

processed_parts = []
for part in parts:
    dt1 = 0
    exp = 1

    for h in range(n):
        for w in range(n):
            if part[h][w] != exp:
                dt1 += 1
            exp = (exp+1) % 2

    dt2 = 0
    for h in range(n):
        for w in range(n):
            if part[h][w] != exp:
                dt2 += 1
            exp = (exp+1) % 2

    processed_parts.append([dt1, dt2])

ans = n*n*4

for i in range(3):
    for j in range(i+1, 4):
        a = 0
        for k, part in enumerate(processed_parts):
            if k == i or k == j:
                a += part[0]
            else:
                a += part[1]
        ans = min(ans, a)

print(ans)