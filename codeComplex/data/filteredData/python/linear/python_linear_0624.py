def main(n):
    # Ensure n is at least 2 so that m >= 1 and n >= 1
    if n < 2:
        n = 2

    # Map n to input sizes: let m = n // 2, n1 = n - m so that n1 + m = n
    m = n // 2
    n1 = n - m

    # Total length of xi and ti is n1 + m
    n2 = n1 + m

    # Deterministic construction of ti:
    # First n1 entries are 0, next m entries are 1
    ti = [0] * n2
    for i in range(n1, n2):
        ti[i] = 1

    # Deterministic construction of xi:
    # xi[i] = i * 2
    xi = [i * 2 for i in range(n2)]

    ai = [0] * (m + 2)
    ar = [0] * (m + 2)
    ar[-1] = 10 ** 11
    ar[0] = -100000000000
    j = 1
    for i in range(n2):
        if ti[i] == 1:
            ar[j] = xi[i]
            j += 1
    i1 = 0
    i2 = 1
    for i in range(n2):
        if ti[i] == 1:
            i2 += 1
            i1 += 1
            continue
        num = xi[i] - ar[i1]
        num2 = ar[i2] - xi[i]
        if num <= num2:
            ai[i1] += 1
        else:
            ai[i2] += 1

    # Keep the same output format as original: ai[1..m] space-separated
    out = []
    for i in range(1, m + 1):
        out.append(str(ai[i]))
    print(" ".join(out))


if __name__ == "__main__":
    # Example deterministic call; change n here for experiments
    main(10)