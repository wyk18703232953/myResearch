def main(n):
    from itertools import combinations
    from collections import defaultdict

    # Deterministic generation of n and m
    # Interpret n as the number of rows; set m as a simple function of n
    m = max(2, (n % 10) + 2)

    # Deterministic generation of matrix a with size n x m
    # Ensure varying values but fully deterministic and scalable
    a = [[(i * m + j) % (5 * m) + 1 for j in range(m)] for i in range(n)]

    mx = max(max(row) for row in a)

    if n == 1:
        print(1, 1)
        return

    l = 0
    r = mx + 1
    while l + 1 < r:
        flg = 0
        x = (l + r) // 2
        jud = set()
        dc = defaultdict(int)
        for i in range(n):
            jnum = 0
            for j in range(m):
                if a[i][j] >= x:
                    jnum += 1 << j
            if dc[jnum] == 0:
                dc[jnum] = i + 1
            if jnum == (1 << m) - 1:
                flg = 1
                if i == 0:
                    ans = (i + 1, i + 2 if i + 2 <= n else 1)
                else:
                    ans = (1, i + 1)
            jud.add(jnum)
        for p, q in combinations(jud, 2):
            if p | q == (1 << m) - 1:
                flg = 1
                ans = (dc[p], dc[q])
        if flg:
            l = x
        else:
            r = x
    if l == 0:
        # If no positive threshold found, fall back to a deterministic pair
        print(1, 2 if n >= 2 else 1)
    else:
        print(*ans)


if __name__ == "__main__":
    main(1000)