import random

def main(n: int):
    # 生成测试数据：随机生成 n 行 n 列由 '.' 和 '*' 构成的地图
    m = n
    MAP = []
    for _ in range(n):
        row = []
        for _ in range(m):
            # 简单随机：'*' 概率 1/3
            row.append('*' if random.randint(0, 2) == 0 else '.')
        MAP.append(row)

    # 以下为原逻辑，仅将输入改为使用生成的 MAP、n、m
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
        print(-1)
    else:
        ANSLIST = []
        for i in range(n):
            for j in range(m):
                if ANS[i][j] != 0:
                    ANSLIST.append((i + 1, j + 1, ANS[i][j] - 1))

        print(len(ANSLIST))
        for ans in ANSLIST:
            print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)