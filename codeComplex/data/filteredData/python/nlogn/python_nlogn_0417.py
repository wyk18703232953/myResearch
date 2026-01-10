def main(n):
    from collections import defaultdict, Counter

    # Deterministic generation of n intervals
    # Example pattern: l = i, r = i + (i % 5) + 1  (ensures r > l)
    a = defaultdict(list)
    count_left = Counter()
    count_right = Counter()

    for i in range(1, n + 1):
        l = i
        r = i + (i % 5) + 1
        count_left[l] += 1
        count_right[r] += 1

    count = [0] * (n + 1)

    if not count_left and not count_right:
        print(' '.join(map(str, count[1:])))
        return

    pts = sorted(set(count_left.keys()) | set(count_right.keys()))
    c = 0
    prev = pts[0]
    for pt in pts:
        if count_left[pt]:
            count[c] += pt - prev - 1
            c += count_left[pt]
            count[c] += 1
            c -= count_right[pt]
        else:
            count[c] += pt - prev
            c -= count_right[pt]
        prev = pt

    print(' '.join(map(str, count[1:])))


if __name__ == "__main__":
    main(10)