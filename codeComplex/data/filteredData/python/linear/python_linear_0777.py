def main(n):
    # Deterministic data generation based on n
    # Interpret n as m (number of positions in p)
    # Set k as a small constant, and generate p as first m positive integers
    if n <= 0:
        return 0
    m = n
    k = max(1, n // 5)  # ensure k >= 1
    # p is a sequence of m increasing positive integers
    p = tuple(i + 1 for i in range(m))

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
    main(10)