#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import stdout
import random


def main(n: int):
    """
    将交互式程序改为离线可测的版本：
    - n 为偶数（原题要求 n 为 2 的倍数的一半周期），这里按一般偶数处理。
    - 自动生成长度为 n 的测试数组 a。
    - 模拟原本的交互接口 ask / ans。
    """
    assert n % 2 == 0, "n 必须为偶数（因为代码中使用了 n//2 的对置位置）"

    # 1. 生成测试数据 a
    # 为了可重复性，可固定随机种子或自定义构造；这里选择平滑随机序列
    random.seed(0)
    # 生成一个随机数组，范围在 [-10, 10]
    a = [random.randint(-10, 10) for _ in range(n)]

    # 如果想测试“确实有解”的情况，可以人为构造一个位置 mid 使其与对置值相等：
    # 例如：
    # mid = n // 4
    # a[mid + n // 2] = a[mid]

    ask_count = 0  # 统计查询次数

    def ask(num: int) -> int:
        nonlocal ask_count
        # 原题是 1-based 索引，这里保持一致
        ask_count += 1
        val = a[num - 1]
        # 模拟交互输出（可注释掉）
        # print(f"? {num} -> {val}")
        # stdout.flush()
        return val

    def ans(num: int):
        # 输出最终答案
        print("! " + str(num))
        stdout.flush()

    def opposite(num: int) -> int:
        return num + n // 2

    # 原始逻辑开始
    low = 1
    high = opposite(low)
    lval = ask(low)
    hval = ask(high)
    prev_l_less_h = (lval < hval)

    while high - low > 1:
        mid = (low + high) // 2

        lval = ask(mid)
        hval = ask(opposite(mid))
        l_less_h = (lval < hval)

        if abs(lval - hval) % 2 == 1:
            ans(-1)
            return
        elif hval == lval:
            ans(mid)
            return
        else:
            if l_less_h == prev_l_less_h:
                low = mid
            else:
                high = mid

    ans(-1)


if __name__ == "__main__":
    # 示例：调用 main(16)
    # 按需修改 n 测试不同规模
    main(16)