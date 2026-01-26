def main(n):
    # Interpret n as grid size: n x n
    # Ensure n >= 1
    if n <= 0:
        return

    # Deterministically construct a pattern of '*' and '.' with size n x n
    # Use a simple arithmetic pattern so it's reproducible and non-trivial
    grid = []
    for i in range(n):
        row_chars = []
        for j in range(n):
            # Example deterministic pattern: star if (i*j + i + j) is even
            if (i * j + i + j) % 2 == 0:
                row_chars.append('*')

            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))

    # Now run the original logic, interpreting:
    # n = number of rows, m = number of columns
    m = n
    ll = [c == '*' for _ in range(n) for c in grid[_]]
    nm = n * m
    RLUD = [*[range(i, i + m) for i in range(0, nm, m)],
            *[range(i, nm, m) for i in range(m)]]
    cc = [1000] * nm
    for f in True, False:
        for r in RLUD:
            v = 0
            for i in r:
                if ll[i]:
                    v += 1
                    if cc[i] > v:
                        cc[i] = v

                else:
                    v = cc[i] = 0
        if f:
            ll.reverse()
            cc.reverse()
    cc = [c if c != 1 else 0 for c in cc]
    for f in True, False:
        for r in RLUD:
            v = 0
            for i in r:
                if v > cc[i]:
                    v -= 1

                else:
                    v = cc[i]
                if v:
                    ll[i] = False
        if f:
            ll.reverse()
            cc.reverse()
    if any(ll):
        # print(-1)
        pass

    else:
        res = []
        for i, c in enumerate(cc):
            if c:
                res.append(f'{i//m+1} {i%m+1} {c-1}')
        # print(len(res), '\n'.join(res), sep='\n')
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different experiment scales
    main(5)