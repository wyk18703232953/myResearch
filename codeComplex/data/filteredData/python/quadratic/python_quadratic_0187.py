def main(n):
    a = [i for i in range(1, n + 1)]
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i):
            f[i][j] = f[i - 1][j] ^ f[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            f[i][j] = max(f[i][j], f[i - 1][j], f[i - 1][j + 1])
    q = n
    outputs = []
    for i in range(q):
        l = 1
        r = min(n, i + 1)
        outputs.append(str(f[r - l][l - 1]))
    # print("\n".join(outputs))
    pass
if __name__ == "__main__":
    main(10)