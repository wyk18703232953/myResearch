def main(n):
    # n controls the scale: we set array length = n, and choose m deterministically
    if n <= 0:
        return

    # Choose m as a positive integer depending on n (e.g., about sqrt(n), at least 1)
    m = max(1, int(n**0.5))

    # Deterministically generate array a of length n
    # Example pattern: a[i] = (i * (i + 3)) % (2 * m + 1)
    base = 2 * m + 1
    a = [(i * (i + 3)) % base for i in range(n)]

    t = n // m
    remain = [[] for _ in range(m)]
    for i in range(n):
        x = a[i] % m
        remain[x].append(i)
    ans = 0
    f = []
    for i in range(2 * m):
        cur = i % m
        while len(remain[cur]) > t:
            elm = remain[cur].pop()
            f.append([elm, i])
        while len(remain[cur]) < t and len(f) != 0:
            elm, j = f.pop()
            remain[cur].append(elm)
            delta = abs(i - j)
            a[elm] += delta
            ans += delta

    # Output kept for determinism / correctness check
    # print(ans)
    pass
    # print(*a)
    pass
if __name__ == "__main__":
    # Example deterministic call for timing experiments
    main(10_000)