from bisect import bisect_left
import random


def main(n):
    # n: number of elements in v
    # We generate:
    #   - v: n random integers in [1, 10**9]
    #   - m: number of "queries" (here chosen as a function of n)
    #   - h: derived from m randomly generated triples (x1, x2, _)

    MAX = 10**9

    # Generate v: n random integers, then sort
    v = sorted(random.randint(1, MAX) for _ in range(n))

    # Choose m relative to n; here m = max(1, 2*n) for a non-trivial size
    m = max(1, 2 * n)

    # Generate m triples (x1, x2, _) and collect h where x1 == 1
    h = []
    for _ in range(m):
        x1 = random.randint(1, 2)        # so roughly half will be 1
        x2 = random.randint(1, MAX + 1)  # can exceed MAX to test that branch
        _unused = 0                      # third value not used in logic
        if x1 == 1:
            h.append(x2)

    h.sort()
    lh = len(h)

    if lh == 0:
        result = 0
    elif n == 0:
        result = lh - bisect_left(h, MAX)
    else:
        result = n + lh - bisect_left(h, MAX)
        for i in range(n):
            result = min(result, lh - bisect_left(h, v[i]) + i)

    print(result)


if __name__ == '__main__':
    # Example: run with some default n
    main(10)