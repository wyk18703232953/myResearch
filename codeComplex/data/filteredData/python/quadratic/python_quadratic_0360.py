def main(n):
    # Interpret n as size parameter: build a grid with
    # rows = n, cols = max(1, n) to ensure at least 1 column
    rows = n
    cols = max(1, n)
    nm = rows * cols

    # Deterministic pattern: '*' if (i + j) % 3 == 0 else '.'
    ll = []
    for i in range(rows):
        for j in range(cols):
            ll.append(((i + j) % 3) == 0)

    RLUD = [*[range(i, i + cols) for i in range(0, nm, cols)],
            *[range(i, nm, cols) for i in range(cols)]]
    cc = [1000] * nm

    for f in (True, False):
        for r in RLUD:
            v = 0
            for i in r:
                if ll[i]:
                    v += 1
                    if cc[i] > v:
                        cc[i] = v

                else:
                    v = 0
                    cc[i] = 0
        if f:
            ll.reverse()
            cc.reverse()

    cc = [c if c != 1 else 0 for c in cc]

    for f in (True, False):
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
                res.append(f'{i // cols + 1} {i % cols + 1} {c - 1}')
        # print(len(res), '\n'.join(res), sep='\n')
        pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)