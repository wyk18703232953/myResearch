def has(x, bit):
    return x & (1 << bit)


def solve(l, r):
    bit = 62
    while bit >= 0 and has(l, bit) == has(r, bit):
        bit -= 1
    return 2 ** (bit + 1) - 1


def main(n):
    # n controls the scale of generated test data
    # We generate n deterministic test cases with pairs (l, r)
    results = []
    for i in range(1, n + 1):
        # Deterministic construction of l and r
        # Ensure l <= r and values grow with i
        l = i
        r = 2 * i + (i // 2)
        results.append(solve(l, r))
    # To keep behavior similar to typical solutions, print results
    for res in results:
        # print(res)
        pass
    return results


if __name__ == "__main__":
    main(10)