#!/usr/bin/env python3
import random

def main(n, k=None, value_range=(0, 100)):
    """
    n: 数据规模（行数）
    k: 目标位置（1-based），若为 None，则随机生成 1..n 之间的值
    value_range: 每行第一个元素的取值范围 (min, max)
    """
    if n <= 0:
        return 0

    if k is None:
        k = random.randint(1, n)
    else:
        k = max(1, min(k, n))  # 保证 1 <= k <= n

    # 生成测试数据：每行生成一个二元组 [score, something]
    # score 用于排序，something 用于打破同分的排序稳定性
    ais = []
    for _ in range(n):
        score = random.randint(*value_range)
        other = random.randint(*value_range)
        ais.append([score, other])

    ais.sort(key=lambda x: (-x[0], x[1]))
    target = ais[k - 1]
    return ais.count(target)


if __name__ == "__main__":
    # 示例：n=10，k=3
    result = main(10, 3)
    print(result)