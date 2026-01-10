def main(n):
    # Interpret n as the size of both X and Y
    # n must be at least 1
    if n <= 0:
        return 0

    # Deterministic generation of n and m
    m = n

    # Generate X: n integers in descending-related pattern after sort
    # Example pattern: X[i] = (3*i) % (10**6 + 3)
    X = [(3 * i) % (10**6 + 3) for i in range(n)]

    # Generate Y: m queries, each is a pair [type, value]
    # We include some type=1 with value=10**9, some with other values, and some with other types
    Y = []
    for i in range(m):
        if i % 5 == 0:
            # Roughly 1/5 are special (1, 10**9)
            Y.append([1, 10**9])
        elif i % 3 == 0:
            # Some type=1 with varying values
            Y.append([1, (i * 7) % (10**6 + 7) + 1])
        else:
            # Other types
            Y.append([2, (i * 11) % (10**6 + 33) + 2])

    Z = []
    ANS = 0
    for y in Y:
        if y[0] == 1 and y[1] == 10**9:
            ANS += 1
        elif y[0] == 1:
            Z.append(y[1])

    X.sort(reverse=True)
    Z.sort(reverse=True)

    XCOUNT = [0] * n

    i = 0
    j = 0
    l = len(Z)
    X.append(0)
    Z.append(0)
    while i < l + 1 and j < n:
        if Z[i] >= X[j]:
            i += 1
        else:
            XCOUNT[j] = i
            j += 1

    count = n
    XCOUNT.reverse()
    for i in range(n):
        if count > i + XCOUNT[i]:
            count = i + XCOUNT[i]

    result = count + ANS
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10_000)