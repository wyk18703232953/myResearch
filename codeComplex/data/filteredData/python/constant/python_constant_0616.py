import math
import random

def main(n):
    # 生成测试数据：n 对区间 [l, r]
    # 这里生成 1 <= l <= r <= 2 * n 的随机区间
    intervals = []
    for _ in range(n):
        l = random.randint(1, 2 * n)
        r = random.randint(l, 2 * n)
        intervals.append((l, r))

    # 原逻辑处理
    for l, r in intervals:
        l -= 1
        war1 = math.ceil(l / 2)
        if l % 2 == 1:
            war1 = -1 * war1

        war2 = math.ceil(r / 2)
        if r % 2 == 1:
            war2 = -1 * war2

        print(war2 - war1)


# 示例运行（可根据需要调整或移除）
if __name__ == "__main__":
    main(5)