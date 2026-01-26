def main(n):
    from functools import reduce

    # Map n to problem scale:
    # n: number of entries
    # m: capacity-like parameter, chosen deterministically as 3*n//2
    m = 3 * n // 2

    # Deterministically generate entries as pairs (a, b)
    # Ensure a >= b so that a-b is non-negative, like typical greedy setups
    entries = []
    for i in range(1, n + 1):
        a = i + (i // 2)
        b = i // 2
        entries.append((a, b, a - b))

    entries.sort(key=lambda x: x[2], reverse=True)

    size = reduce(lambda s, e: s + e[0], entries, 0)
    count = 0

    while size > m and count < n:
        size -= entries[count][2]
        count += 1

    return -1 if size > m else count


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    # print(result)
    pass