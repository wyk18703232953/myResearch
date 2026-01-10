def main(n):
    from collections import Counter

    # Interpret n as the size of the array x; let k = n for scalability
    k = n

    # Deterministic generation of x: repeating pattern of small integers
    # Example pattern: 1, 2, 3, ..., 10, 1, 2, ...
    pattern_size = 10 if n >= 10 else max(1, n)
    x = [(i % pattern_size) + 1 for i in range(n)]

    dd = Counter()
    for i in range(k):
        dd[x[i]] = dd[x[i]] + 1

    final = 0
    for i in range(1, k + 1):
        ans = 0
        d = dd.copy()
        for j in range(n):
            for jj in d:
                if d[jj] >= i:
                    d[jj] -= i
                    ans = ans + 1
                    break
        if ans >= n:
            final = i
        else:
            break

    print(final)


if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(1000)