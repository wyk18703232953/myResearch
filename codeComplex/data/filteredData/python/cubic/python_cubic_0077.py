from collections import deque
import random

def main(n):
    # 生成规模为 n 的测试数据：
    # n 行 m 列的网格，m 与 n 同规模
    m = n

    # 随机生成 k（1 到 n 之间）
    k = max(1, n // 3)
    k = min(k, n * m)  # 不超过格子总数

    # 随机生成 k 个起始点（不重复）
    points = set()
    while len(points) < k:
        x = random.randrange(n)
        y = random.randrange(m)
        points.add((x, y))
    points = list(points)
    k = len(points)  # 实际数量

    # 模拟原代码逻辑
    a = [[0] * m for _ in range(n)]
    dq = deque()

    # 原代码将坐标从 1-based 转成 0-based，我们直接用 0-based
    # line 数组按 [x1,y1,x2,y2,...] 形式
    line = []
    for x, y in points:
        line.append(x)
        line.append(y)

    for i in range(0, 2 * k, 2):
        a[line[i]][line[i + 1]] = 1
        dq.append((line[i], line[i + 1]))

    x, y = -1, -1
    while dq:
        x, y = dq.popleft()
        for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= tx < n and 0 <= ty < m and not a[tx][ty]:
                a[tx][ty] = 1
                dq.append((tx, ty))

    # 输出与原程序一致：最终填满时最后一个点的 1-based 坐标
    print(f'{x+1} {y+1}')


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)