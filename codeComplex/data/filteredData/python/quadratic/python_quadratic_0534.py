def main(n):
    # n controls the size of the arrays
    # ensure minimal valid size
    if n < 3:
        n = 3

    # Define number of '1's in b (m) as a function of n
    m = max(2, n // 3)

    # Deterministic construction of a and b
    # a: strictly increasing sequence
    a = [i * 2 for i in range(n)]

    # b: length n, with exactly m positions set to 1, others 0
    # place 1 at positions: 0, n//m, 2*n//m, ...
    b = [0] * n
    step = max(1, n // m)
    ones_positions = []
    idx = 0
    while len(ones_positions) < m and idx < n:
        ones_positions.append(idx)
        idx += step
    # if we still don't have m ones due to rounding, fill remaining at the end
    extra_needed = m - len(ones_positions)
    if extra_needed > 0:
        # fill from the end backwards, avoiding duplicates
        pos = n - 1
        while extra_needed > 0 and pos >= 0:
            if pos not in ones_positions:
                ones_positions.append(pos)
                extra_needed -= 1
            pos -= 1
    ones_positions = sorted(set(ones_positions))[:m]
    # ensure exactly m ones
    if len(ones_positions) < m:
        # pad from the start if still short
        pos = 0
        while len(ones_positions) < m and pos < n:
            if pos not in ones_positions:
                ones_positions.append(pos)
            pos += 1
        ones_positions = sorted(ones_positions)[:m]
    for pos in ones_positions:
        b[pos] = 1

    def next_pos(k, arr):
        i = k + 1
        while i < len(arr) and arr[i] != 1:
            i += 1
        return i

    ans = [0] * (m + 1)

    k = -1
    k = next_pos(k, b)
    ans[1] = k
    for i in range(2, m + 1):
        kk = next_pos(k, b)
        # guard in case of malformed b (should not happen with our construction)
        if kk >= n:
            kk = n - 1
        for j in range(k + 1, kk):
            if a[j] - a[k] <= a[kk] - a[j]:
                ans[i - 1] += 1
            else:
                ans[i] += 1
        k = kk

    ans[m] += (n + m - 1 - k)

    for i in range(1, m + 1):
        print(ans[i], end=' ')
    print()


if __name__ == "__main__":
    # example call with n = 20
    main(20)