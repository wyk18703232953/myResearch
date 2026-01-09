def main(n):
    # Interpret n as:
    # number of elements m = n
    # page size k = max(1, n // 10) for scaling
    # maximum value range for elements roughly ~ n * 2
    m = n
    if m <= 0:
        # print(0)
        pass
        return

    k = max(1, n // 10)

    # Deterministic generation of P:
    # P[i] are distinct and within [1, 2*m]
    # Use arithmetic pattern to avoid randomness
    P = [((i * 3) % (2 * m)) + 1 for i in range(m)]
    P = sorted(set(P))  # ensure distinct and sorted ascending
    # Adjust m in case duplicates removed by set
    m = len(P)

    P = P[:]  # list
    P.reverse()

    ops = 0
    i = 1
    while P:
        nxt = P[-1]
        togo = nxt - i
        if togo > 0:
            skip = togo // k * k
            i += skip

        space = k
        while space:
            special = 0
            while P and P[-1] < i + space:
                special += 1
                P.pop()
            i += space
            if not special:
                break
            ops += 1
            space = special

    # print(ops)
    pass
if __name__ == "__main__":
    # Example call for scaling experiment
    main(10000)