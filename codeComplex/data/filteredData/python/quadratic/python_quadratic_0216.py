def main(n):
    # Interpret n as both rows and columns
    if n <= 0:
        return
    r = n
    c = n

    # Deterministic grid generation: '0' and '1' characters
    # Pattern: a[i][j] = '1' if (i + j) % 2 == 0 else '0'
    a = []
    for i in range(r):
        row_chars = []
        for j in range(c):
            if (i + j) % 2 == 0:
                row_chars.append('1')

            else:
                row_chars.append('0')
        a.append(''.join(row_chars))

    pre = [[0 for _ in range(c)] for _ in range(r)]
    suf = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(c):
        pre[0][i] = int(a[0][i])
        suf[r - 1][i] = int(a[r - 1][i])

    for i in range(1, r):
        for j in range(c):
            pre[i][j] = pre[i - 1][j] + int(a[i][j])

    for i in range(r - 2, -1, -1):
        for j in range(c):
            suf[i][j] = suf[i + 1][j] + int(a[i][j])

    ans = 'NO'
    for i in range(r):
        f = 1
        for j in range(c):
            up = 0
            down = 0
            if i - 1 >= 0:
                up = pre[i - 1][j]
            if i + 1 < r:
                down = suf[i + 1][j]
            if up + down == 0:
                f = 0
                break
        if f:
            ans = "YES"
            break
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)