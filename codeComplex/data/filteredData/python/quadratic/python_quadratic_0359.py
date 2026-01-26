def main(n):
    # Define grid size based on n
    if n <= 0:
        n = 1
    rows = n
    cols = n

    # Deterministically generate a grid pattern of '*' and '.'
    # Example pattern: '*' when (i + j) % 3 != 0, '.' otherwise
    s = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i * 2 + j * 3) % 5 == 0:
                row.append('.')

            else:
                row.append('*')
        s.append(row)

    n = rows
    m = cols

    u = [[-1 for _ in range(m)] for _ in range(n)]
    d = [[-1 for _ in range(m)] for _ in range(n)]
    l = [[-1 for _ in range(m)] for _ in range(n)]
    r = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        acum = 0
        for j in range(n):
            if s[j][i] == ".":
                acum = 0

            else:
                acum += 1
            u[j][i] = acum

    for i in range(m):
        acum = 0
        for j in range(n - 1, -1, -1):
            if s[j][i] == ".":
                acum = 0

            else:
                acum += 1
            d[j][i] = acum

    for i in range(n):
        acum = 0
        for j in range(m):
            if s[i][j] == ".":
                acum = 0

            else:
                acum += 1
            l[i][j] = acum

    for i in range(n):
        acum = 0
        for j in range(m - 1, -1, -1):
            if s[i][j] == ".":
                acum = 0

            else:
                acum += 1
            r[i][j] = acum

    ans = []
    t1 = [[0 for _ in range(m)] for _ in range(n)]
    t2 = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            d1 = min(l[i][j], r[i][j], u[i][j], d[i][j]) - 1
            if d1 > 0:
                ans.append([i + 1, j + 1, d1])
                if i + d1 < n:
                    t1[i + d1][j] += 1
                if i - d1 >= 0:
                    t1[i - d1][j] -= 1
                if j - d1 >= 0:
                    t2[i][j - d1] += 1
                if j + d1 < m:
                    t2[i][j + d1] -= 1

    dp = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        acum = 0
        for j in range(m):
            acum += t2[i][j]
            if acum != 0 or t2[i][j] != 0:
                dp[i][j] = '*'

    for i in range(m):
        acum = 0
        for j in range(n):
            acum += t1[j][i]
            if acum != 0 or t1[j][i] != 0:
                dp[j][i] = '*'

    if dp != s:
        # print(-1)
        pass
        return

    # print(len(ans))
    pass
    for triple in ans:
        # print(*triple)
        pass
if __name__ == "__main__":
    main(5)