import random

def main(n):
    # 生成一个大致为 n x n 的随机地图（# 或 .）
    m = n
    MAP = [[random.choice(['#', '.']) for _ in range(m)] for _ in range(n)]

    ANSMAP = [["." for _ in range(m)] for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (
                MAP[i - 1][j - 1] == "#" and MAP[i - 1][j] == "#" and MAP[i - 1][j + 1] == "#" and
                MAP[i][j - 1] == "#" and MAP[i][j + 1] == "#" and
                MAP[i + 1][j - 1] == "#" and MAP[i + 1][j] == "#" and MAP[i + 1][j + 1] == "#"
            ):
                ANSMAP[i - 1][j - 1] = "#"
                ANSMAP[i - 1][j] = "#"
                ANSMAP[i - 1][j + 1] = "#"
                ANSMAP[i][j - 1] = "#"
                ANSMAP[i][j + 1] = "#"
                ANSMAP[i + 1][j - 1] = "#"
                ANSMAP[i + 1][j] = "#"
                ANSMAP[i + 1][j + 1] = "#"

    if MAP == ANSMAP:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例运行
    main(5)