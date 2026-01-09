def main(n):
    # Deterministically generate n and q, and array a of length n
    # Here we set q proportional to n for scalability
    if n < 2:
        return

    q = n * 2
    # Generate a strictly increasing sequence so that M = a[-1]
    a = [(i * 2 + 1) % (10**9 + 7) for i in range(n)]

    M = max(a)
    i = 0
    x = a[0]
    L = []
    L1 = []
    L2 = []
    while x != M:
        L1.append(x)
        L2.append(a[i + 1])
        i = i + 1
        if x < a[i]:
            L.append(x)
            x = a[i]

        else:
            L.append(a[i])

    b = a[i + 1:] + L

    # Deterministically generate q queries
    # Use a simple pattern that covers small, around i, and large values
    queries = []
    if i == 0:
        base = 1

    else:
        base = i
    for j in range(q):
        if j < q // 3:
            m = j + 1
        elif j < 2 * q // 3:
            m = base + j

        else:
            m = n + j
        queries.append(m)

    output_lines = []
    for m in queries:
        if m <= i:
            output_lines.append(str(L1[m - 1]) + " " + str(L2[m - 1]))

        else:
            output_lines.append(str(x) + " " + str(b[(m - i - 1) % (n - 1)]))

    # Print all results to keep behavior similar to original
    # print("\n".join(output_lines))
    pass
if __name__ == "__main__":
    main(10)