def main(n):
    # Interpret n as the scale parameter for lengths of x, y, z.
    # Keep within reasonable bounds to avoid huge memory use.
    a = n
    b = n
    c = n

    # Deterministic data generation using arithmetic patterns
    x = [(i * 2 + 1) for i in range(a)]
    y = [(i * 3 + 2) for i in range(b)]
    z = [(i * 5 + 3) for i in range(c)]

    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)

    a += 1
    b += 1
    c += 1

    x = [0] + x
    y = [0] + y
    z = [0] + z

    tmp = [[0] * c for _ in range(b)]
    best = [tmp[:] for _ in range(a)]
    for i in range(a):
        best[i] = [row[:] for row in tmp]

    ans = 0

    for i in range(a):
        for j in range(b):
            for k in range(c):
                if (i + j + k) % 2 == 0:
                    aa = 0
                    bb = 0
                    cc = 0
                    if i > 0 and j > 0:
                        aa = best[i - 1][j - 1][k] + x[i] * y[j]
                    if i > 0 and k > 0:
                        bb = best[i - 1][j][k - 1] + x[i] * z[k]
                    if j > 0 and k > 0:
                        cc = best[i][j - 1][k - 1] + y[j] * z[k]

                    best[i][j][k] = max(aa, bb, cc)
                    if best[i][j][k] > ans:
                        ans = best[i][j][k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(5)