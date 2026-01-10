def main(n):
    # Deterministically generate n intervals [l, r] with 1-based indices
    # Pattern ensures variety and deterministic behavior
    intervals = []
    for i in range(1, n + 1):
        l = i
        r = i + (i % 5) + (i // 3)
        intervals.append((l, r, i))

    a = []
    for l, r, idx in intervals:
        a.append([l, -r, idx])

    a.sort()
    hh = a[0][1]
    wahh = max(-1, a[0][2])
    for i in range(1, n):
        if a[i][1] >= hh:
            print(a[i][2], wahh)
            return
        else:
            hh = a[i][1]
            wahh = a[i][2]
    print(-1, -1)


if __name__ == "__main__":
    main(10)