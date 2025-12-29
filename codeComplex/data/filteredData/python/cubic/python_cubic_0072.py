from collections import deque
import random

def main(n):
    # 1. 根据规模 n 生成测试数据
    # 这里设定：网格大小 n x n，起点个数 k = max(1, n // 5)
    # 起点随机生成，且不重复
    m = n
    k = max(1, n // 5)

    # 所有合法格子 (1..n, 1..m)
    all_cells = [(i, j) for i in range(1, n + 1) for j in range(1, m + 1)]
    random.shuffle(all_cells)
    starts = all_cells[:k]  # k 个起点

    # 2. 原逻辑：从多个起点进行 BFS，找到最后被访问到的格子
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()

    # v 为 (n+2) x (m+2) 的边界填充矩阵，1 表示未访问，0 表示已访问或边界
    v = [[1] * (m + 2) for _ in range(n + 2)]
    for i in range(m + 2):
        v[0][i] = 0
        v[-1][i] = 0
    for i in range(n + 2):
        v[i][0] = 0
        v[i][-1] = 0

    # 将起点加入队列并标记
    for (sx, sy) in starts:
        q.append((sx, sy))
        v[sx][sy] = 0

    last_x, last_y = -1, -1
    while q:
        x, y = q.popleft()
        last_x, last_y = x, y
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if v[xx][yy]:
                v[xx][yy] = 0
                q.append((xx, yy))

    # 3. 返回/打印结果：最后访问到的格子坐标
    # 为便于使用，这里返回结果；也可改成 print(last_x, last_y)
    return last_x, last_y


# 简单示例：当作为脚本直接运行时，给一个默认规模测试
if __name__ == "__main__":
    res = main(10)
    print(res[0], res[1])