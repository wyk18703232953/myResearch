#!/usr/bin/env python3

def main(n):
    # Interpret n as both number of rows and columns for scalability
    if n <= 0:
        return

    # Deterministically generate n x n matrix with varying values
    # Example pattern: a[i][j] = (i * 17 + j * 31) % (2*n + 1)
    # Ensures some spread of values and a well-defined max.
    m = n
    array = []
    max_val = 0
    mod = 2 * n + 1
    for i in range(n):
        line = []
        base_i = i * 17
        for j in range(m):
            val = (base_i + j * 31) % mod
            line.append(val)
        array.append(line)
        row_max = max(line)
        if row_max > max_val:
            max_val = row_max

    good = (1 << m) - 1
    l = 0
    r = max_val + 1
    a = 0
    b = 0

    while r - l > 1:
        mid = (l + r) // 2
        bit_array = dict()
        for k, line in enumerate(array):
            val = 0
            for i, item in enumerate(line):
                if item >= mid:
                    val |= 1 << i
            bit_array[val] = k
        ok = False
        i = j = 0
        keys = list(bit_array.keys())
        for key1 in keys:
            if ok:
                break
            for key2 in keys:
                if key1 | key2 == good:
                    ok = True
                    i = bit_array[key1]
                    j = bit_array[key2]
                    break
        if ok:
            a = i
            b = j
            l = mid
        else:
            r = mid

    print(a + 1, b + 1)


if __name__ == "__main__":
    main(200)