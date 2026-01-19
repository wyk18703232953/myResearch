import sys
from itertools import combinations
from collections import defaultdict

def main(n):
    # 解释规模映射：
    # 使用较小的 m 以保证位运算 (1<<m) 不会过大
    # n 控制矩阵的总规模：n = 行数 * 列数 的近似
    if n <= 1:
        n = 2

    # 设定列数 m 为不超过 20 的值，以便组合状态数量可控
    m = min(10, max(2, int(n ** 0.5)))
    rows = max(2, n // m)

    # 确定性生成矩阵 a[rows][m]
    # 每个元素使用简单算术构造，保证整体可重复、确定
    a = [[(i + 1) * (j + 2) + (i // 2) + (j * j) for j in range(m)] for i in range(rows)]

    n_rows = rows
    mx = max(max(a[i]) for i in range(n_rows))
    if n_rows == 1:
        print(1, 1)
        return

    l = 0
    r = mx + 1
    while l + 1 < r:
        flg = 0
        x = (l + r) // 2
        jud = set()
        dc = defaultdict(int)
        for i in range(n_rows):
            jnum = 0
            for j in range(m):
                if a[i][j] >= x:
                    jnum += 1 << j
            if dc[jnum] == 0:
                dc[jnum] = i + 1
            if jnum == (1 << m) - 1:
                flg = 1
                if i == 0:
                    ans = (i + 1, i + 2)
                else:
                    ans = (1, i + 1)
            jud.add(jnum)
        for p, q in combinations(jud, 2):
            if p | q == (1 << m) - 1:
                flg = 1
                ans = (dc[p], dc[q])
        if flg:
            l = x
        else:
            r = x
    if l == 0:
        print(1, 2)
    else:
        print(*ans)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 用于不同规模实验
    main(1000)