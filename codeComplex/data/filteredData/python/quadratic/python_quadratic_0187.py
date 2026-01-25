def main(n):
    # derive sizes from n
    length = max(1, n // 2)
    q = max(1, n - length)

    # deterministic generation of array a
    a = [(i * 17 + 23) % 1000 for i in range(length)]

    f = [[0] * length for _ in range(length)]
    for i in range(length):
        f[0][i] = a[i]
    for i in range(1, length):
        for j in range(length - i):
            f[i][j] = f[i - 1][j] ^ f[i - 1][j + 1]
    for i in range(1, length):
        for j in range(length - i):
            val = f[i][j]
            if f[i - 1][j] > val:
                val = f[i - 1][j]
            if f[i - 1][j + 1] > val:
                val = f[i - 1][j + 1]
            f[i][j] = val

    # deterministic queries covering the range
    outputs = []
    if length == 1:
        for _ in range(q):
            outputs.append(str(f[0][0]))
    else:
        for i in range(q):
            l = i % length + 1
            r = length - (i % length)
            if l > r:
                l, r = r, l
            outputs.append(str(f[r - l][l - 1]))

    print("\n".join(outputs))


if __name__ == "__main__":
    main(10)