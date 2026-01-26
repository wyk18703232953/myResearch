def main(n):
    a = [[(i * n + j + 1) / (n * n) for j in range(n)] for i in range(n)]
    masks = dict()
    big = 2 ** n - 1

    if n == 1:
        print(1)
        return

    for i in range(n):
        for j in range(i + 1, n):
            masks[big ^ (1 << j)] += a[i][j]
            masks[big ^ (1 << i)] += a[j][i]

    def get_bit(x, i):
        return (x >> i) & 1

    for _ in range(2, n):
        tem = dict()
        for msk in masks:
            for bit in range(n):
                if get_bit(msk, bit):
                    s = 0.0
                    for i in range(n):
                        if get_bit(msk, i):
                            s += a[i][bit]
                    tem[msk ^ (1 << bit)] += s * masks[msk]
        masks = tem

    su = sum(masks.values())
    if su == 0:
        print(*([0.0] * n))
    else:
        print(*[masks[2 ** i] / su for i in range(n)])


if __name__ == "__main__":
    main(5)