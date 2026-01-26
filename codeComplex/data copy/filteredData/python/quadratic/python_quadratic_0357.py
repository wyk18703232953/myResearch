def main(n):
    # Interpret n as both number of rows and columns
    if n <= 0:
        return
    r = n
    c = n

    # Deterministic generation of the grid s (r x c)
    # Pattern: '*' if (i + j) % 3 == 0 else '.'
    s = []
    for i in range(r):
        row = []
        for j in range(c):
            if (i + j) % 3 == 0:
                row.append("*")

            else:
                row.append(".")
        s.append(row)

    t = [[1000] * c for _ in range(r)]
    ok1 = [[0] * c for _ in range(r)]
    ok2 = [[0] * c for _ in range(r)]

    for i in range(r):
        si = s[i]
        cnt = 0
        for j in range(c):
            if si[j] == "*":
                cnt += 1

            else:
                cnt = 0
            if cnt < t[i][j]:
                t[i][j] = cnt
        cnt = 0
        for j in range(c - 1, -1, -1):
            if si[j] == "*":
                cnt += 1

            else:
                cnt = 0
            if cnt < t[i][j]:
                t[i][j] = cnt

    for j in range(c):
        cnt = 0
        for i in range(r):
            if s[i][j] == "*":
                cnt += 1

            else:
                cnt = 0
            if cnt < t[i][j]:
                t[i][j] = cnt
        cnt = 0
        for i in range(r - 1, -1, -1):
            if s[i][j] == "*":
                cnt += 1

            else:
                cnt = 0
            if cnt < t[i][j]:
                t[i][j] = cnt

    ans = []
    for i in range(r):
        for j in range(c):
            tij = t[i][j] - 1
            if tij >= 1:
                ans.append((i + 1, j + 1, tij))
                up = i - tij
                if up < 0:
                    up = 0
                ok1[up][j] += 1
                down = i + tij + 1
                if down < r:
                    ok1[down][j] -= 1
                left = j - tij
                if left < 0:
                    left = 0
                ok2[i][left] += 1
                right = j + tij + 1
                if right < c:
                    ok2[i][right] -= 1

    for i in range(1, r):
        for j in range(c):
            ok1[i][j] += ok1[i - 1][j]
    for i in range(r):
        for j in range(1, c):
            ok2[i][j] += ok2[i][j - 1]

    for i in range(r):
        for j in range(c):
            if s[i][j] == "*":
                if not (ok1[i][j] or ok2[i][j]):
                    # print(-1)
                    pass
                    return

    k = len(ans)
    # print(k)
    pass
    for ans0 in ans:
        # print(ans0[0], ans0[1], ans0[2])
        pass
if __name__ == "__main__":
    main(5)