def main(n):
    # Ensure n is at least 1 to avoid empty ranges
    if n <= 0:
        print(0)
        return

    # Deterministic parameter setup based on n
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic array a of length n
    a = [(i * 2 + 1) for i in range(n)]

    t = 0
    for i in range(3, (1 << n) + 1):
        c = i
        count = 0
        while c != 0:
            c = c & (c - 1)
            count += 1
        if count > 1:
            subset_values = []
            s = 0
            for j in range(n):
                if i & (1 << j):
                    val = a[j]
                    s += val
                    subset_values.append(val)
            if subset_values:
                if l <= s <= r and (max(subset_values) - min(subset_values)) >= x:
                    t += 1
    print(t)


if __name__ == "__main__":
    main(10)