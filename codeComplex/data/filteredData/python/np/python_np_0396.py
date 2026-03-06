def main(n):
    from collections import defaultdict as dd

    # Interpret n as the number of rows; choose m as a small logarithmic function of n (at least 1)
    m = max(1, (n.bit_length() + 1) // 2)

    # Deterministically generate matrix l1 of size n x m
    # Values are constructed using simple arithmetic so they are large enough to exercise the binary search logic
    l1 = [[(i + 1) * (j + 2) + (i ^ j) for j in range(m)] for i in range(n)]

    l = 0
    h = 10 ** 9
    c = 2 ** m - 1
    x, y = 1, 2

    while l <= h:
        mid = (l + h) // 2
        d = dd(int)
        d1 = dd(int)
        for i in range(n):
            s_bits = []
            for j in range(m):
                if l1[i][j] >= mid:
                    s_bits.append('1')
                else:
                    s_bits.append('0')
            s = int(''.join(s_bits), 2)
            d[s] += 1
            d1[s] = i + 1
        f = 0
        for i_key in d:
            for j_key in d:
                if i_key | j_key == c:
                    f = 1
                    x = d1[i_key]
                    y = d1[j_key]
                    break
            if f:
                break
        if f:
            if l == h:
                break
            l = mid + 1
        else:
            if l == h:
                break
            h = mid
    print(x, y)


if __name__ == "__main__":
    main(1000)