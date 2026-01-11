import math
import collections
import bisect

def main(n):
    # Interpret n as the number of items; derive m deterministically from n
    # Original input: n, m then n pairs (a, b)
    # Here we deterministically generate:
    # m: some function of n
    # a, b: deterministic sequences based on i and n
    m = n * (n + 1) // 4

    space = 0
    saved = []
    for i in range(n):
        # Deterministic generation of a and b
        a = (i + 1) * 2
        b = (i % (n + 1))  # ensure b <= a for many i, but not necessary
        space += a
        saved.append(a - b)

    saved.sort(reverse=True)

    if space - sum(saved) > m:
        # print(-1)
        pass
        return

    if space <= m:
        # print(0)
        pass
        return

    i = 0
    count = 0
    while i < n:
        count += 1
        space -= saved[i]
        if space <= m:
            # print(count)
            pass
            break
        i += 1


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)