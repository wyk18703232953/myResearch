def main(n):
    # Interpret n as: original n = n, and number of operations m = n
    orig_n = n
    m = n

    res = 0
    mx = (orig_n - 1) * orig_n // 2
    if orig_n & 1:
        mn = (orig_n // 2) * (orig_n // 2 + 1)

    else:
        mn = orig_n * orig_n // 4

    # Deterministic generation of (x, d) pairs
    for i in range(m):
        x = i  # x grows linearly with i
        d = (i % 3) - 1  # cycles through -1, 0, 1
        res += x * orig_n
        if d > 0:
            res += mx * d

        else:
            res += mn * d

    # print('%.10f' % (res / orig_n))
    pass
if __name__ == "__main__":
    main(10)