def main(n):
    # Interpret n as grid size: n x n
    # Ensure at least 1x1 grid
    if n <= 0:
        return

    # Generate a deterministic n x n MAP of '.' and '*'
    # Pattern: cell is '*' if (i + j) % 3 == 0, else '.'
    m = n
    MAP = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 3 == 0:
                row.append('*')

            else:
                row.append('.')
        MAP.append(row)

    T0 = [[0] * (m + 1) for _ in range(n + 1)]
    T1 = [[0] * (m + 1) for _ in range(n + 1)]
    Y0 = [[0] * (m + 1) for _ in range(n + 1)]
    Y1 = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if MAP[i][j] == "*":
                T0[i][j] = T0[i - 1][j] + 1
                Y0[i][j] = Y0[i][j - 1] + 1

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if MAP[i][j] == "*":
                T1[i][j] = T1[i + 1][j] + 1
                Y1[i][j] = Y1[i][j + 1] + 1

    ANS = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            score = min(T0[i][j], T1[i][j], Y0[i][j], Y1[i][j])
            if score >= 2:
                ANS[i][j] = score

    T0 = [[0] * (m + 1) for _ in range(n + 1)]
    T1 = [[0] * (m + 1) for _ in range(n + 1)]
    Y0 = [[0] * (m + 1) for _ in range(n + 1)]
    Y1 = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            T0[i][j] = max(ANS[i][j], T0[i - 1][j] - 1)
            Y0[i][j] = max(ANS[i][j], Y0[i][j - 1] - 1)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            T1[i][j] = max(ANS[i][j], T1[i + 1][j] - 1)
            Y1[i][j] = max(ANS[i][j], Y1[i][j + 1] - 1)

    SUF = [["."] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if T0[i][j] or T1[i][j] or Y0[i][j] or Y1[i][j]:
                SUF[i][j] = "*"

    if SUF != MAP:
        # print(-1)
        pass

    else:
        ANSLIST = []
        for i in range(n):
            for j in range(m):
                if ANS[i][j] != 0:
                    ANSLIST.append((i + 1, j + 1, ANS[i][j] - 1))

        # print(len(ANSLIST))
        pass
        for ans in ANSLIST:
            # print(*ans)
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)