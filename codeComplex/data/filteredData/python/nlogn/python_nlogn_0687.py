def main(n):
    # Interpret n as both number of boys and girls
    # Ensure minimum size for logic requiring at least 2 boys and 1 girl
    if n < 2:
        n = 2
    m = n

    # Deterministic generation of b and g
    # b: increasing sequence, g: shifted and scaled based on b
    b = [i for i in range(1, n + 1)]
    g = [i + n for i in range(1, m + 1)]

    b.sort()
    g.sort()
    if b[-1] > g[0]:
        print(-1)
        return
    a = 0
    a += sum(g) - g[0]
    if g[0] == b[-1]:
        a += g[0]
        a += m * sum(b[:-1])
        print(a)
    else:
        if len(b) < 2:
            # Fallback, though with our generation this shouldn't happen
            print(-1)
            return
        a += g[0]
        a += m * sum(b[:-2]) + (m - 1) * b[-2] + b[-1]
        print(a)


if __name__ == "__main__":
    main(10)