import random

def main(n):
    # 生成规模为 n 的测试数据：
    # p: 4 个点的矩形（x1 y1 x2 y2 x3 y3 x4 y4）
    # d: 4 个点的菱形（x1 y1 ... x4 y4）
    # 坐标范围控制在 [-50, 50]，加 100 后落在 [50, 150] 内，以适配 201x201 的 grid

    # 生成矩形 p
    # 保证是轴对齐矩形，4 点顺序为 左下, 左上, 右上, 右下
    minx = random.randint(-50, 40)
    maxx = random.randint(minx + 1, 50)
    miny = random.randint(-50, 40)
    maxy = random.randint(miny + 1, 50)
    p_raw = [minx, miny, minx, maxy, maxx, maxy, maxx, miny]
    p = [coord + 100 for coord in p_raw]

    # 生成菱形 d
    # 设中心 (cx, cy)，水平宽度 2*span，4 个点为左右上下
    cx = random.randint(-40, 40)
    cy = random.randint(-40, 40)
    span = random.randint(1, 10)
    left  = (cx - span, cy)
    right = (cx + span, cy)
    up    = (cx, cy + span)
    down  = (cx, cy - span)
    d_raw = [left[0], left[1], right[0], right[1], up[0], up[1], down[0], down[1]]
    d = [coord + 100 for coord in d_raw]

    # 原始逻辑开始
    minx = min(p[::2])
    maxx = max(p[::2])
    miny = min(p[1::2])
    maxy = max(p[1::2])

    grid = [[False] * 201 for _ in range(201)]
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if 0 <= x < 201 and 0 <= y < 201:
                grid[x][y] = True

    minx = min(d[::2])
    maxx = max(d[::2])
    avgx = sum(d[::2]) // 4
    avgy = sum(d[1::2]) // 4
    span = (maxx - minx) // 2

    for x in range(minx, maxx + 1):
        if not (0 <= x < 201):
            continue
        height = span - abs(x - avgx)
        for y in range(avgy - height, avgy + height + 1):
            if 0 <= y < 201 and grid[x][y]:
                print('YES')
                return

    print('NO')


if __name__ == "__main__":
    # 示例：调用 main，n 当前未参与逻辑，可用作规模控制或随机种子等
    main(10)