def main(n):
    # Interpret n as the number of columns; deterministically set k based on n
    # Here, k is chosen as roughly n to scale with input size while staying valid
    k = max(0, min(n * 2, (n - 2) * 2))  # ensure within reasonable bounds

    cols = n
    out = [['.'] * cols for _ in range(4)]
    kk = k

    if kk & 1 and cols > 0:
        out[1][cols >> 1] = '#'
        kk -= 1

    for i in range(1, 3):
        l, r = 1, cols - 2
        for j in range(1, cols - 2):
            if kk:
                kk -= 1
                if j & 1:
                    out[i][l] = '#'
                    l += 1

                else:
                    out[i][r] = '#'
                    r -= 1

    for i in range(1, 3):
        if kk and cols > 0:
            kk -= 1
            out[i][cols >> 1] = '#'

    # print('YES')
    pass
    # print('\n'.join(''.join(row) for row in out))
    pass
if __name__ == "__main__":
    main(10)