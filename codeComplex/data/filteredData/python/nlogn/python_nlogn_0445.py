def main(n):
    # Deterministically generate data based on n
    # n is the length of the array p
    if n <= 0:
        print(0)
        return 0

    # Choose m deterministically as n // 2
    m = n // 2

    # Generate p such that:
    # - For indices < m: values < m
    # - Index == m: value == m (if m < n)
    # - For indices > m: values > m
    p_values = []
    for i in range(n):
        if i < m:
            p_values.append(m - 1)
        elif i == m:
            p_values.append(m)
        else:
            p_values.append(m + 1)

    def intCompare(x):
        if int(x) == m:
            return 0
        if int(x) < m:
            return -1
        return 1

    p = list(map(intCompare, p_values))

    ret = 0
    ind = p.index(0)
    tem = 0
    MAX_SIZE = 400001
    OFFSET = 200000  # to safely index negative sums if they appear

    ret0 = [0] * MAX_SIZE
    ret1 = [0] * MAX_SIZE
    set0 = set()

    # From ind down to 0
    for i in range(ind, -1, -1):
        tem += p[i]
        idx = tem + OFFSET
        if 0 <= idx < MAX_SIZE:
            ret0[idx] += 1
            set0.add(tem)

    tem = 0
    # From ind up to n-1
    for i in range(ind, n):
        tem += p[i]
        idx = tem + OFFSET
        if 0 <= idx < MAX_SIZE:
            ret1[idx] += 1

    for val in set0:
        i0 = val + OFFSET
        i1 = -val + OFFSET
        i2 = 1 - val + OFFSET
        c0 = ret0[i0] if 0 <= i0 < MAX_SIZE else 0
        c1 = ret1[i1] if 0 <= i1 < MAX_SIZE else 0
        c2 = ret1[i2] if 0 <= i2 < MAX_SIZE else 0
        ret += c0 * (c1 + c2)

    print(ret)
    return 0

if __name__ == "__main__":
    main(10)