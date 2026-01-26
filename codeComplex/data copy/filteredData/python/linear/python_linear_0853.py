import sys

def main(n):
    # Interpret n as the length of array a.
    # Deterministically construct m, k, and a based on n.
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 3)          # number of buckets, derived from n
    k = n                       # constant increment, derived from n

    # Build a deterministic array a[1..n]; a[0] is unused placeholder
    # Example: a[i] = (i % 7) + 1
    a = [None] + [(i % 7) + 1 for i in range(1, n + 1)]

    # Prefix sums
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i]

    # Core algorithm (unchanged)
    INF = 10 ** 16
    s = [INF for _ in range(m)]
    s[0] = k
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, p[i] - min(s))
        idx = i % m
        if s[idx] > p[i]:
            s[idx] = p[i]
        s[idx] += k
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)