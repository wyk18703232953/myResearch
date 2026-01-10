from math import gcd

DXY = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # L,D,R,Uの順番

def on_one_line(Points):
    n = len(Points)
    s = set([])
    for i in range(1, n):
        x, y = Points[i][0] - Points[0][0], Points[i][1] - Points[0][1]
        g = gcd(x, y)
        x //= g
        y //= g
        if x < 0:
            x *= -1
            y *= -1
        if x == 0:
            y = abs(y)
        s.add((x, y))
    return len(s) == 1

def solve(Ps):
    n = len(Ps)
    if n <= 2:
        return "YES"
    if on_one_line(Ps):
        return "YES"

    p, q = Ps[1][0] - Ps[0][0], Ps[1][1] - Ps[0][1]
    g = gcd(p, q)
    p //= g
    q //= g
    if p < 0:
        p *= -1
        q *= -1
    elif p == 0:
        q = abs(q)

    not_same = []
    for i in range(2, n):
        x, y = Ps[i][0] - Ps[0][0], Ps[i][1] - Ps[0][1]
        gx = gcd(x, y)
        x, y = x // gx, y // gx
        if x < 0:
            x *= -1
            y *= -1
        if x == 0:
            y = abs(y)
        if (x, y) != (p, q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        return "YES"

    if on_one_line(not_same):
        return "YES"

    p, q = not_same[0][0] - Ps[0][0], not_same[0][1] - Ps[0][1]
    P, Q = not_same[0]
    g = gcd(p, q)
    p //= g
    q //= g
    if p < 0:
        p *= -1
        q *= -1
    elif p == 0:
        q = abs(q)
    not_same = []

    for i in range(n):
        x, y = Ps[i][0] - Ps[0][0], Ps[i][1] - Ps[0][1]
        if x == 0 and y == 0:
            continue
        gx = gcd(x, y)
        x, y = x // gx, y // gx
        if x < 0:
            x *= -1
            y *= -1
        if x == 0:
            y = abs(y)
        if (x, y) != (p, q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        return "YES"

    if on_one_line(not_same):
        return "YES"

    p, q = P - Ps[1][0], Q - Ps[1][1]
    g = gcd(p, q)
    p //= g
    q //= g
    if p < 0:
        p *= -1
        q *= -1
    elif p == 0:
        q = abs(q)

    not_same = []
    for i in range(n):
        x, y = Ps[i][0] - Ps[1][0], Ps[i][1] - Ps[1][1]
        if x == 0 and y == 0:
            continue
        gx = gcd(x, y)
        x, y = x // gx, y // gx
        if x < 0:
            x *= -1
            y *= -1
        if x == 0:
            y = abs(y)
        if (x, y) != (p, q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        return "YES"

    if on_one_line(not_same):
        return "YES"

    return "NO"

def generate_points(n):
    if n <= 0:
        return []
    if n == 1:
        return [(0, 0)]
    if n == 2:
        return [(0, 0), (1, 1)]
    pts = []
    for i in range(n):
        if i == 0:
            pts.append((0, 0))
        elif i == 1:
            pts.append((1, 1))
        elif i == 2:
            pts.append((2, 2))
        else:
            x = i
            y = (i * i + i) // 2
            pts.append((x, y))
    return pts

def main(n):
    Ps = generate_points(n)
    ans = solve(Ps)
    print(ans)

if __name__ == "__main__":
    main(10)