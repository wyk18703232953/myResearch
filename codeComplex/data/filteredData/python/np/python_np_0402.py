import sys

def generate_data(n):
    # Interpret n as both number of rows and columns
    if n <= 0:
        n = 1
    m = n
    a = [[(i * m + j) % 1000000007 for j in range(m)] for i in range(n)]
    return n, m, a

def main(n):
    n, m, a = generate_data(n)

    ok = 0
    ng = 10**9 + 1
    judge = (1 << m) - 1
    dg = 1000

    while ng - ok > 1:
        mid = (ng + ok) // 2
        tank = set()
        for i in range(n):
            r = 0
            for j in range(m):
                r *= 2
                if a[i][j] >= mid:
                    r += 1
            tank.add(r)

        updated = False
        for p in tank:
            for q in tank:
                if p | q == judge:
                    ok = mid
                    updated = True
                    break
            if updated:
                break
        if not updated:
            ng = mid

    tank = set()
    res = []
    for i in range(n):
        r = 0
        for j in range(m):
            r *= 2
            if a[i][j] >= ok:
                r += 1
        if r not in tank:
            res.append(i * dg + r)
        tank.add(r)

    for p in res:
        for q in res:
            if (p % dg) | (q % dg) == judge:
                print(p // dg + 1, q // dg + 1)
                return

if __name__ == "__main__":
    # example call for experimental use
    main(5)