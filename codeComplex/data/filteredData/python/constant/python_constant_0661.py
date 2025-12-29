import random

def main(n: int):
    # 根据规模 n 生成三点 (ax, ay), (bx, by), (cx, cy)
    # 为了让路径长度与 n 有控制关系，这里约定：
    # - x 坐标在 [0, n] 范围内
    # - y 坐标在 [0, n] 范围内
    # 并保证三点的 x 坐标不全部相同，以避免退化成竖线
    while True:
        ax, ay = random.randint(0, n), random.randint(0, n)
        bx, by = random.randint(0, n), random.randint(0, n)
        cx, cy = random.randint(0, n), random.randint(0, n)
        if not (ax == bx == cx):
            break

    # 以下为原逻辑
    if ax > bx:
        ax, bx = bx, ax
        ay, by = by, ay
    if ax > cx:
        ax, cx = cx, ax
        ay, cy = cy, ay
    if bx > cx:
        bx, cx = cx, bx
        by, cy = cy, by

    ans = []
    for i in range(min(ay, by, cy), max(ay, by, cy) + 1):
        ans.append([bx, i])
    for i in range(ax, bx):
        ans.append([i, ay])
    for i in range(bx + 1, cx + 1):
        ans.append([i, cy])

    print(len(ans))
    for x, y in ans:
        print(x, y)


if __name__ == "__main__":
    # 示例：n=10，可根据需要修改
    main(10)