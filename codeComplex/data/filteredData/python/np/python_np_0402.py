def main(n):
    # Interpret n as number of rows; derive m deterministically from n
    # Ensure m >= 1
    m = max(1, (n % 10) + 1)

    # Deterministic matrix generation: a[i][j] grows with i,j
    a = [[(i + 1) * (j + 2) % 1000000007 for j in range(m)] for i in range(n)]

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
                r <<= 1
                if a[i][j] >= mid:
                    r += 1
            tank.add(r)

        updated = False
        for p in tank:
            if updated:
                break
            for q in tank:
                if (p | q) == judge:
                    ok = mid
                    updated = True
                    break
        if not updated:
            ng = mid

    tank = set()
    res = []
    for i in range(n):
        r = 0
        for j in range(m):
            r <<= 1
            if a[i][j] >= ok:
                r += 1
        if r not in tank:
            res.append(i * dg + r)
        tank.add(r)

    for p in res:
        for q in res:
            if (p % dg) | (q % dg) == judge:
                # Keep the print to preserve original behavior
                print(p // dg + 1, q // dg + 1)
                return


if __name__ == "__main__":
    # Example deterministic call; change n here to scale input size
    main(1000)