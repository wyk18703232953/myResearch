from collections import deque
import random

def main(n):
    # 生成数据：
    # 用 n 作为规模参数，构造一个大致为 n×n 的网格
    # m 同 n，k 取一个与 n 成比例的值，随机选 k 个起点
    m = n

    # 起点数量，至少 1，至多 n*n 的一半
    max_k = max(1, (n * n) // 2)
    k = max(1, min(n, max_k))

    # 随机生成 k 个不同的起点坐标，范围 [1, n]×[1, m]
    points = set()
    while len(points) < k:
        x = random.randint(1, n)
        y = random.randint(1, m)
        points.add((x, y))
    a = []
    for x, y in points:
        a.append(x)
        a.append(y)

    # 以下是原 main 的逻辑，去掉文件 IO，直接返回结果
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()

    v = [[1] * (m + 2) for _ in range(n + 2)]
    for i in range(m + 2):
        v[0][i] = 0
        v[-1][i] = 0
    for i in range(n + 2):
        v[i][0] = 0
        v[i][-1] = 0

    for i in range(0, 2 * k, 2):
        x0, y0 = a[i], a[i + 1]
        q.append((x0, y0))
        v[x0][y0] = 0

    # BFS
    last_x, last_y = None, None
    while q:
        x, y = q.popleft()
        last_x, last_y = x, y
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if v[xx][yy]:
                q.append((xx, yy))
                v[xx][yy] = 0

    # 返回最后一次弹出的坐标
    return last_x, last_y

# 示例：直接运行本文件时做一个简单测试
if __name__ == "__main__":
    n = 5
    result = main(n)
    print(result)