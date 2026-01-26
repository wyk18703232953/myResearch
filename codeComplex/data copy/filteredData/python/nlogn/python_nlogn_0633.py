def main(n):
    # Interpret n as total length of original input arrays x and t (n + m in original code)
    # We need positive n; for n <= 2, the logic degenerates, so enforce minimum size
    if n < 4:
        n = 4

    # We will construct a valid split into original n_r (number of r elements) and m (number of d elements)
    # Let m = n // 3 (at least 1), n_r = n - m
    m = max(1, n // 3)
    n_r = n - m

    # Generate arrays r (size n_r) and d (size m) deterministically, strictly increasing
    r = [i * 2 + 1 for i in range(n_r)]          # odd numbers: 1,3,5,...
    d = [i * 3 for i in range(m)]                # multiples of 3: 0,3,6,...

    # Now reconstruct the original x and t arrays of total length n_r + m
    # We interleave elements of r and d in increasing order of values to produce a mixed sequence.
    i_r = 0
    i_d = 0
    x = [0] * (n_r + m)
    t = [0] * (n_r + m)  # 0 for r, 1 for d

    idx = 0
    while i_r < n_r and i_d < m:
        if r[i_r] <= d[i_d]:
            x[idx] = r[i_r]
            t[idx] = 0
            i_r += 1

        else:
            x[idx] = d[i_d]
            t[idx] = 1
            i_d += 1
        idx += 1
    while i_r < n_r:
        x[idx] = r[i_r]
        t[idx] = 0
        i_r += 1
        idx += 1
    while i_d < m:
        x[idx] = d[i_d]
        t[idx] = 1
        i_d += 1
        idx += 1

    # Now run the original logic with these constructed x and t
    r_arr = [0] * n_r
    d_arr = [0] * m
    countr = 0
    countd = 0
    for i in range(n_r + m):
        if int(t[i]) == 1:
            d_arr[countd] = int(x[i])
            countd += 1

        else:
            r_arr[countr] = int(x[i])
            countr += 1

    current = 0
    count = [0] * m
    for i in range(n_r):
        while current < m - 1:
            if d_arr[current + 1] >= r_arr[i]:
                break
            current += 1
        if current == m - 1:
            count[m - 1] += (n_r - i)
            break
        if 2 * r_arr[i] <= (d_arr[current] + d_arr[current + 1]):
            count[current] += 1

        else:
            count[current + 1] += 1

    s = ""
    for i in range(m):
        s += str(count[i]) + " "
    # print(s[:-1])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(1000)