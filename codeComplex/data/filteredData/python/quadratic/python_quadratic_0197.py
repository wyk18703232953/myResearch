def main(n):
    # Generate deterministic input data based on n
    # Original: n, array ar of length n, then q queries
    # Here: q = n, ar[i] = i+1, queries are (l, r) covering all ranges of length >=1
    if n <= 0:
        return
    ar = [i + 1 for i in range(n)]

    li = []
    for i in range(n):
        xx = []
        for j in range(n - i):
            xx.append(0)
        li.append(xx.copy())

    for i in range(n):
        for j in range(n - i):
            if i == 0:
                li[i][j] = ar[j]

            else:
                li[i][j] = li[i - 1][j] ^ li[i - 1][j + 1]

    for i in range(1, n):
        for j in range(n - i):
            li[i][j] = max(li[i][j], li[i - 1][j], li[i - 1][j + 1])

    # Deterministic query generation:
    # Use all intervals (l, r) with 1 <= l <= r <= n in lexicographic order,
    # but limit to at most n queries to keep scale tied to n.
    queries = []
    for length in range(1, n + 1):
        if len(queries) >= n:
            break
        for l in range(1, n - length + 2):
            if len(queries) >= n:
                break
            r = l + length - 1
            queries.append((l, r))

    for l, r in queries:
        # print(li[r - l][l - 1])
        pass
if __name__ == "__main__":
    # Example deterministic run
    main(5)