def main(n):
    # Interpret n as the length of p
    if n <= 0:
        return 0

    # Deterministically construct n, m, k, and p:
    # Keep k as a small constant for page size analogy
    k = 3

    # Construct p as the first n positive integers
    p = tuple(i + 1 for i in range(n))

    # Let m be the maximum element implied by p
    m = max(p)

    d = 0
    part = (p[0] - 1) // k
    moves = 0
    skip = 0

    for pi in p:
        if (pi - 1 - d) // k == part:
            skip += 1
            continue
        d += skip
        part = (pi - 1 - d) // k
        skip = 1
        moves += 1

    result = moves + 1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)