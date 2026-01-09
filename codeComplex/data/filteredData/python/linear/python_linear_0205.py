def main(n):
    # Deterministic data generation
    # Interpret n as the number of (hour, minute) entries
    # Generate s and n time points in non-decreasing order
    s = n % 60 + 1  # waiting time, at least 1 and at most 60

    h = []
    m = []
    l = [0]

    # Generate times: base minutes increase deterministically with i
    # Ensure they are non-decreasing and within a day
    base_gap = max(1, 1440 // (n + 1))
    for i in range(n):
        total_minutes = base_gap * (i + 1)
        total_minutes %= 1440
        x = total_minutes // 60
        y = total_minutes % 60
        h.append(x)
        m.append(y)
        l.append(total_minutes)

    # Original logic
    if l[1] != 0 and (l[1] - l[0]) >= s + 1:
        # print(0, 0)
        pass

    else:
        k = 2 * s + 2
        r = 0
        for i in range(n):
            if l[i + 1] - l[i] >= k:
                r = l[i] + s + 1
                break

            else:
                continue
        if r == 0:
            r = l[n] + s + 1
        # print(r // 60, r % 60)
        pass
if __name__ == "__main__":
    main(10)