import math

ceil1 = lambda a, b: (a + b - 1) // b
get_bit = lambda x, i: (x >> i) & 1


class dict_float(dict):
    def __missing__(self, key):
        return 0.0


def generate_matrix(n):
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            val = ((i * 131 + j * 97 + 17) % 1000) / 10.0
            row.append(val)
        a.append(row)
    return a


def core_logic(n, a):
    masks = dict_float()
    big = 2 ** n - 1

    if n == 1:
        return [1.0]

    for i in range(n):
        for j in range(i + 1, n):
            masks[big ^ (1 << j)] += a[i][j]
            masks[big ^ (1 << i)] += a[j][i]

    for _ in range(2, n):
        tem = dict_float()
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
        return [0.0 for _ in range(n)]
    return [masks[1 << i] / su for i in range(n)]


def main(n):
    if n <= 0:
        return []
    n = int(n)
    a = generate_matrix(n)
    res = core_logic(n, a)
    for x in res:
        print(x, end=" ")
    print()
    return res


if __name__ == "__main__":
    main(4)