import sys

def main(n):
    # Map n to a reasonable (n, m)
    # Ensure m >= 1 and not too large; here choose m = max(1, min(20, n))
    m = max(1, min(20, n))
    n_rows = n
    mask = (1 << m) - 1

    # Deterministic generation of matrix l with size n_rows x m
    # Values are simple functions of (i, j) to keep everything reproducible
    l = [[(i * 131 + j * 73) % 1000 for j in range(m)] for i in range(n_rows)]

    lo = -1  # Possible
    hi = 10 ** 9 + 1  # Impossible

    outi = 0
    outj = 0

    while hi - lo > 1:
        test = (hi + lo) // 2

        things = dict()
        for i in range(n_rows):
            curr = 0
            for v in l[i]:
                curr *= 2
                if v >= test:
                    curr += 1
            things[curr] = i

        works = False
        for v1 in things:
            for v2 in things:
                if v1 | v2 == mask:
                    outi = things[v1]
                    outj = things[v2]
                    works = True
                    break
            if works:
                break

        if works:
            lo = test
        else:
            hi = test

    # Keep output format compatible with original program
    print(outi + 1, outj + 1)


if __name__ == "__main__":
    # Example call; you can change 10 to any desired scale
    main(10)