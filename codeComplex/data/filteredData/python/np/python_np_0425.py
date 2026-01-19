#!/usr/bin/env python3

def main(n):
    # n controls: number of rows and number of columns (square matrix n x n)
    # Values are deterministic based on i, j, and n.
    if n <= 0:
        return

    max_val = 0
    rows = n
    cols = n
    array = []

    for i in range(rows):
        line = []
        for j in range(cols):
            # Deterministic value construction
            val = (i + 1) * (j + 2) + (i // 2) + (j % 3)
            line.append(val)
        array.append(line)
        max_val = max(max_val, max(line))

    good = (1 << cols) - 1
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
        i = 0
        j = 0
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
    # Example deterministic call; adjust n as needed for experiments
    main(5)