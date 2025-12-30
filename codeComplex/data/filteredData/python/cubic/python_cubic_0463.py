import random

def main(n):
    # 这里将规模 n 理解为网格的行数，同时构造一个接近正方形的列数 m
    # 并设置步数 k 与 n 相关，你可以按需要自行调整生成方案
    m = n
    k = 2 * ((n + 1) // 2)  # 保证为偶数，避免原算法全为 -1

    # 生成测试数据：边权为 1~9 的随机正整数
    rlist = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    clist = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    dway = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if k % 2:
        res = [[-1] * m for _ in range(n)]
    else:
        flist = [[0] * m for _ in range(n)]
        for _ in range(k // 2):
            glist = [[10 ** 9] * m for _ in range(n)]
            for dx, dy in dway:
                klist = rlist if dx == 0 else clist
                for x in range(n):
                    for y in range(m):
                        xx, yy = x + dx, y + dy
                        if not (0 <= xx < n) or not (0 <= yy < m):
                            continue
                        tx = xx if dx == -1 else x
                        ty = yy if dy == -1 else y
                        glist[x][y] = min(
                            glist[x][y],
                            flist[xx][yy] + klist[tx][ty] * 2
                        )
            flist = glist
        res = flist

    for row in res:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)