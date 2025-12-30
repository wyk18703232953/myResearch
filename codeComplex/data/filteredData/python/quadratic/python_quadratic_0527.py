import sys
import random

def main(n):
    # 生成一个 m x n 的网格，这里简单取 m = n（也可按需调整）
    m = n

    # 随机生成由 '.' 和 '#' 组成的网格
    # 你可以调整 p 来控制 '#' 的密度
    p = 0.5  # 每个位置是 '#' 的概率
    l = []
    for _ in range(m):
        row = ''.join('#' if random.random() < p else '.' for _ in range(n))
        l.append(row)

    inks = []
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if (
                l[i - 1][j - 1] == '#' and l[i][j - 1] == '#' and l[i + 1][j - 1] == '#' and
                l[i - 1][j] == '#' and                       l[i + 1][j] == '#' and
                l[i - 1][j + 1] == '#' and l[i][j + 1] == '#' and l[i + 1][j + 1] == '#'
            ):
                inks += [
                    (i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
                    (i - 1, j),               (i + 1, j),
                    (i - 1, j + 1), (i, j + 1), (i + 1, j + 1),
                ]

    for i in range(m):
        for j in range(n):
            if l[i][j] == '#' and (i, j) not in inks:
                print("NO")
                return
    print("YES")


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改规模
    main(5)