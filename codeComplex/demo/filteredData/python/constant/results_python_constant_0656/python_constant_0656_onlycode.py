xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
if (xb, yb) < (xa, ya):
    xa, ya, xb, yb = xb, yb, xa, ya
if (xc, yc) < (xa, ya):
    xa, ya, xc, yc = xc, yc, xa, ya
if xb > xc:
    xb, yb, xc, yc = xc, yc, xb, yb
d = 1 if ya <= yc else -1
if ya <= yb <= yc or ya >= yb >= yc:
    print(xc - xa + abs(yc - ya) + 1)
    for x in range(xa, xb):
        print(x, ya)
    for y in range(ya, yc, d):
        print(xb, y)
    for x in range(xb, xc + 1):
        print(x, yc)
elif yb < min(ya, yc):
    print(xc - xa + max(ya, yc) - yb + 1)
    for x in range(xa, xc + 1):
        print(x, min(ya, yc))
    for y in range(yb, min(ya, yc)):
        print(xb, y)
    if ya < yc:
        for y in range(ya + 1, yc + 1):
            print(xc, y)
    else:
        for y in range(yc + 1, ya + 1):
            print(xa, y)
else:
    print(xc - xa + yb - min(ya, yc) + 1)
    for x in range(xa, xc + 1):
        print(x, max(ya, yc))
    for y in range(max(ya, yc) + 1, yb + 1):
        print(xb, y)
    if ya < yc:
        for y in range(ya, yc):
            print(xa, y)
    else:
        for y in range(yc, ya):
            print(xc, y)
