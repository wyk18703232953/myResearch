#!/usr/bin/env python3
import random


def main(n: int) -> int:
    """
    n: 规模参数，用于生成测试数据
       - 垂直线数量 v = n
       - 水平线候选数量 h = n
    返回：算法结果（原程序中最终输出的 res）
    """

    # 生成测试数据
    # 垂直线 v 个：vs 为它们的 x 坐标
    v = n
    h = n

    # 生成 v 个垂直线位置，范围在 [1, 10^6]
    vs = [random.randint(1, 10**6) for _ in range(v)]

    # 生成 h 个水平线候选：(x1, x2, y)
    # 其中一部分满足 x1 == 1，才会被真正使用
    hs_raw = []
    for _ in range(h):
        x1 = 1 if random.random() < 0.7 else random.randint(2, 10**6)
        x2 = random.randint(1, 10**6)
        if x2 < 1:
            x2 = 1
        y = random.randint(1, 10**6)
        hs_raw.append((x1, x2, y))

    # 以下为原始逻辑的复现

    # 排序垂直线并追加 10^9
    vs.sort()
    vs.append(10**9)

    # 过滤出 x1 == 1 的水平线，格式与原程序一致：[x1, x2, y]
    hs = []
    for x1, x2, y in hs_raw:
        if x1 == 1:
            hs.append([x1, x2, y])

    # 按 x2 升序排序
    hs.sort(key=lambda val: val[1])

    hsl = len(hs)
    vsl = len(vs)

    res = v + h
    hi = 0
    for vi, vx in enumerate(vs):
        while hi < hsl and hs[hi][1] < vx:
            hi += 1
        res = min(res, vi + hsl - hi)

    return res


if __name__ == "__main__":
    # 示例：运行 main(10)，实际使用时可修改 n
    result = main(10)
    print(result)