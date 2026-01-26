def main(n):
    # n controls the total size (n + m) of arrays a and t
    # We choose m = max(1, n // 2) so that both a and t have meaningful sizes
    m = max(1, n // 2)
    total = n + m

    # Ensure total is at least 1
    if total <= 0:
        # print()
        pass
        return

    # Generate deterministic array t of length (n + m) with exactly m ones
    # Pattern: first m positions are 1, rest are 0
    t = [1 if i < m else 0 for i in range(total)]

    # Generate deterministic array a of length (n + m)
    # Simple increasing arithmetic pattern based on index
    a = [i * 2 + (i % 3) for i in range(total)]

    ans = [0] * m
    p = []
    for i in range(n + m):
        if t[i] == 1:
            p.append(i)

    # Guard against unexpected situations (though construction should avoid them)
    if not p:
        # print(' '.join(map(str, ans)))
        pass
        return

    ans[0] = p[0]
    for i in range(m):
        if i == m - 1:
            ans[i] += n + m - p[i] - 1

        else:
            for j in range(p[i] + 1, p[i + 1]):
                if a[j] - a[p[i]] <= a[p[i + 1]] - a[j]:
                    ans[i] += 1

                else:
                    ans[i + 1] += 1

    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    main(10)