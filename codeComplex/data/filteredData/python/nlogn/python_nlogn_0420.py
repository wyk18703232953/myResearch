def main(n):
    from collections import defaultdict

    # Deterministic data generation:
    # Generate n intervals [l, r] with 0 <= l <= r, lengths grow with i
    intervals = []
    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        intervals.append((l, r))

    s = []
    for a0, a1 in intervals:
        s += [(a0, 0), (a1, 1)]
    s.sort()

    now, rev = 0, defaultdict(int)
    for a, b in zip(s, s[1:]):
        now += 1 if a[1] == 0 else -1
        if a[1] == 0:
            rev[now] += b[0] - a[0] + (1 if b[1] == 1 else 0)
        elif b[0] != a[0]:
            rev[now] += b[0] - a[0] - (1 if b[1] == 0 else 0)

    for i in range(1, n + 1):
        print(rev[i], end=" ")
    print()


if __name__ == "__main__":
    main(10)