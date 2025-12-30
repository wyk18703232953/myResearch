import random

def main(n):
    # 1. 生成测试数据：n 个线段 [l, r]，l <= r
    segments = []
    for i in range(n):
        l = random.randint(0, 10 * n)
        r = random.randint(l, l + 10)  # 保证 r >= l，区间相对较短
        segments.append((l, r, i + 1))  # 保留原始下标，从 1 开始

    # 2. 按原逻辑排序：先按起点升序，再按终点降序
    segments = sorted(segments, key=lambda x: (x[0], -x[1]))

    # 3. 按原逻辑查找并输出
    for i, seg in enumerate(segments):
        j = i + 1
        if j >= n:
            print("-1 -1")
            return

        while segments[j][1] <= seg[1]:
            print("{} {}".format(segments[j][2], seg[2]))
            return

    print("-1 -1")


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)