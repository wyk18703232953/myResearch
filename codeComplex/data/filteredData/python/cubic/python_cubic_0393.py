from collections import defaultdict
import random

def main(n):
    # 随机生成参数和测试数据
    # n 为行数；列数 m、步数 k 在这里可按需要设定或随机生成
    m = max(1, n)  # 简单设为 m = n（可自行修改为其他规则）
    k = random.randint(1, 2 * n)  # 随机生成一个步数（可根据需要调整范围）

    # 随机生成边权：与原程序读入的数据结构保持一致
    # 水平方向权值：n 行，每行 m-1 个
    horizontal = [
        [random.randint(1, 10) for _ in range(m - 1)]
        for _ in range(n)
    ]
    # 垂直方向权值：n-1 行，每行 m 个
    vertical = [
        [random.randint(1, 10) for _ in range(m)]
        for _ in range(n - 1)
    ]

    dic = defaultdict(lambda: {})

    # 模拟原输入中第一部分：每行 m-1 个数，表示横向相邻格子的权
    for i in range(n):
        line = horizontal[i]
        for j in range(m - 1):
            dic[i * m + j][i * m + j + 1] = line[j] * 2
            dic[i * m + j + 1][i * m + j] = line[j] * 2

    # 模拟原输入中第二部分：每行 m 个数，表示纵向相邻格子的权
    for i in range(n - 1):
        line = vertical[i]
        for j in range(m):
            dic[i * m + j][(i + 1) * m + j] = line[j] * 2
            dic[(i + 1) * m + j][i * m + j] = line[j] * 2

    # 下面是原算法逻辑
    if k % 2 != 0:
        for _ in range(n):
            print(' '.join(('-1',) * m))
        return

    prev = [(0,) * m for _ in range(n)]

    di = (1, 0, -1, 0)
    dj = (0, 1, 0, -1)

    for _ in range(k // 2):
        new = [[100_000_000] * m for _ in range(n)]

        for num in dic:
            i = num // m
            j = num % m
            for idx in range(4):
                ii = i + di[idx]
                jj = j + dj[idx]
                if not (0 <= ii < n and 0 <= jj < m):
                    continue
                new[ii][jj] = min(
                    new[ii][jj],
                    prev[i][j] + dic[i * m + j][ii * m + jj]
                )

        prev = new

    for i in range(n):
        print(' '.join(map(str, prev[i])))


if __name__ == "__main__":
    # 示例：调用 main(3) 规模为 3 的测试
    main(3)