def main(n):
    # Interpret n as the grid width; derive k deterministically from n
    width = max(3, n)  # ensure minimum valid width
    k = (width * 2) // 3  # deterministic function of n

    out = [['.'] * width for _ in range(4)]
    kk = k  # work on a local copy of k, keep original k if needed later

    if kk & 1:
        out[1][width >> 1] = '#'
        kk -= 1

    for i in range(1, 3):
        l, r = 1, width - 2
        for j in range(1, width - 2):
            if kk:
                kk -= 1
                if j & 1:
                    out[i][l] = '#'
                    l += 1

                else:
                    out[i][r] = '#'
                    r -= 1

    for i in range(1, 3):
        if kk:
            kk -= 1
            out[i][width >> 1] = '#'

    # print('YES')
    pass
    # print('\n'.join(''.join(row) for row in out))
    pass
if __name__ == "__main__":
    main(10)